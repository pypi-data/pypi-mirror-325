"""Dora Asset class.

This module defines the Dora Asset class and related functionality.
"""

# pylint: disable=no-member

from os import environ
from typing import Iterator, List, Tuple, Optional

from pydantic import BaseModel, Field, computed_field, ConfigDict
from pydantic_core import PydanticCustomError
from pyiceberg.partitioning import PartitionField, PartitionSpec, Transform
from pyiceberg.schema import Schema
from pyiceberg.catalog import Catalog
from pyiceberg.table import Table as IcebergTable
from pyiceberg.types import TimestampType, StringType, NestedField
from pyiceberg.exceptions import NamespaceAlreadyExistsError, NoSuchTableError
from sqlglot import expressions, parse, exp
from pyarrow import (
    Schema as ArrowSchema,
    schema as arrow_schema,
    Field as ArrowField,
)

from .parser import SQLParser
from .utils import logger

DEFAULT_DIALECT = environ.get('DORA_DEFAULT_DIALECT', 'duckdb')
COLUMN_BREAKPOINT = 1000
META_COLUMN_DATEF = "_data_ts"
META_COLUMN_FRESH = "_load_ts"
META_COLUMN_FILEN = "_file_id"

log = logger(__name__)

class Table(BaseModel):
    """Dora table class.

    Args:
        ast (SQLParser): SQL AST object.
        dialect (str): SQL dialect.
        schema (Schema): Table schema.
        partitions (PartitionSpec): Table partitions.
    """
    ast: SQLParser = Field(description="SQL AST object", exclude=True)
    dialect: str = Field(description="SQL dialect", default=DEFAULT_DIALECT)
    schema: Schema = Field(description="Table schema", default=None)
    partitions: PartitionSpec = Field(description="Table partitions", default=None)
    ref_locations: Optional[List[str]] = Field(description="Reference Locations", default=None)

    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        str_strip_whitespace=True,
        extra="allow")

    def model_post_init(self, *args, **kwargs):  # pylint: disable=unused-argument
        """Post init method."""
        self._validate()  # Check if all requirements are met in the SQL statements
        self.schema = Schema(fields=list(self.meta_fields()) + list(self.data_fields()))
        self.partitions = PartitionSpec(fields=list(self.partition_fields()))
        self.ref_locations = list() # pylint: disable=attribute-defined-outside-init

    def _validate(self) -> None:
        """Validate the mandatory properties."""
        if self.location is None or len(self.location) == 0:
            raise PydanticCustomError("property", "Location is missing in the SQL statement")
        if self.database is None or len(self.database) == 0:
            raise PydanticCustomError("property", "Database is missing in the SQL statement")

    @computed_field
    def name(self) -> str:
        """Extract the table name from a SQL expression.

        Returns:
            str: The table name.
        """
        return f"{self.database}_{self.table}"

    @property
    def is_replace_table(self) -> bool:
        """Check if it is a REPLACE statement.

        Returns:
            bool: True if it is a REPLACE statement, False otherwise.
        """
        return self.ast.ddl.args['replace'] is True

    @property
    def is_query_star(self) -> bool:
        """Check if it is a SELECT * statement.

        Returns:
            bool: True if it is a SELECT * statement, False otherwise.
        """
        return self.ast.ddl.find(expressions.Select).find(expressions.Star) is not None

    @property
    def identifier(self) -> str:
        """Extract the table identifier from a SQL expression.

        Returns:
            str: The table identifier.
        """
        return self.ast.get_table().sql()

    @property
    def table(self) -> str:
        """Extract the table name from a SQL expression.

        Returns:
            str: The table name.
        """
        return self.ast.get_table().name

    @property
    def database(self) -> str:
        """Extract the database name from a SQL expression.

        Returns:
            str: The database name.
        """
        return self.ast.get_table().db

    @property
    def location(self) -> str:
        """Extract the location from a SQL expression.

        Returns:
            str: The location.
        """
        for _location in self.ast.get_location():
            return _location.this

    @property
    def source(self) -> str:
        """Extract the source expression from a SQL expression.

        Returns:
            str: The source expression.
        """
        for _source in self.ast.get_source():
            if isinstance(_source.this, str):
                return _source.this if len(_source.this) > 0 else None
            return _source.this

    @property
    def tags(self) -> list:
        """Extract the tags from a SQL expression.

        Returns:
            list: The tags.
        """
        for _property in self.ast.get_properties():
            key, value = _property.sql().strip().split("=", 1)
            if key.strip().lower() == "tags":
                return value.replace("'", "").strip().split(",")
        return list()

    @property
    def description(self) -> str:
        """Extract the description from a SQL expression.

        Returns:
            str: The description.
        """
        for _description in self.ast.get_description():
            return _description.this
        return str()

    @property
    def references(self) -> List[exp.Table]:
        """Extract the references from a SQL expression.

        Returns:
            exp.Table: The references.
        """
        return list(self.ast.get_foreign_key())

    def query(self, dialect: str = DEFAULT_DIALECT) -> str:
        """Extract the query from a SQL expression.

        Args:
            dialect (str): The SQL dialect.

        Returns:
            str: The query.
        """
        for _q in self.ast.get_query(dialect=dialect):
            return _q

    def meta_fields(self) -> Iterator[NestedField]:
        """Create the metadata fields for the table schema.

        Yields:
            Iterator[NestedField]: An iterator of metadata fields.
        """
        if self.source is not None:
            # Only for source tables
            yield NestedField(
                field_id=COLUMN_BREAKPOINT - 3,
                name=META_COLUMN_FILEN,
                type=StringType(),
                required=False,
                doc="Source file key")
        if self.source is not None:
            # Only for source tables
            yield NestedField(
                field_id=COLUMN_BREAKPOINT - 2,
                name=META_COLUMN_DATEF,
                type=TimestampType(),
                required=False,
                doc="Source file date")
        yield NestedField(
            field_id=COLUMN_BREAKPOINT - 1,
            name=META_COLUMN_FRESH,
            type=TimestampType(),
            required=True,
            doc="Process date")

    def data_fields(self) -> Iterator[NestedField]:
        """Extract the fields from a SQL expression.

        Yields:
            Iterator[NestedField]: An iterator of data fields.
        """
        for idx, col in enumerate(self.ast.get_columns()):
            yield NestedField(
                field_id=idx + 1,
                name=col.name,
                type=self.ast.column_type(col),
                required=self.ast.column_required(col),
                doc=self.ast.column_comment(col))

    def partition_fields(self) -> Iterator[PartitionField]:
        """Extract the partitions from a SQL expression.

        Yields:
            Iterator[PartitionField]: An iterator of partition fields.
        """
        for idx, part in enumerate(self.ast.get_partitions()):
            _transform = self.ast.partition_transform(part)
            if isinstance(part, expressions.Identifier):
                _name = part.find(expressions.Identifier).this
            else:
                _name = part.find(expressions.Column).name
            yield PartitionField(
                source_id=self.schema.find_field(_name).field_id,
                field_id=idx + COLUMN_BREAKPOINT,
                name=f"{_name}_{_transform}",
                transform=_transform)

    def properties(self, comments: bool = False, source: bool = True) -> dict:
        """Extract the properties from a SQL expression.

        Args:
            comments (bool): Whether to include comments.
            source (bool): Whether to include source information.

        Returns:
            dict: The properties.
        """
        _properties = dict()
        for _property in self.ast.get_properties():
            key, value = _property.sql().strip().split("=", 1)
            if key.strip().lower() != "tags":
                _properties[key.lower().strip()] = value.replace("'", "").strip()
        # Add table comments
        if comments and len(self.description) > 0:
            _properties["Description"] = self.description
        # Add source information
        if source:
            _properties["source"] = self.source
        return _properties

    def partition_specs(self) -> Iterator[Tuple[str, Transform, str]]:
        """Extract the iceberg partition spec from a SQL expression.

        Yields:
            Iterator[Tuple[str, Transform, str]]: An iterator of partition specs.
        """
        for _part in self.ast.get_partitions():
            if isinstance(_part, expressions.Identifier):
                _name = _part.find(expressions.Identifier).this
            else:
                _name = _part.find(expressions.Column).name
            _transform = self.ast.partition_transform(_part)
            yield (_name, _transform, f"{_name}_{_transform}")

    def update(self, catalog: Catalog, schema: ArrowSchema) -> IcebergTable:
        """Create the iceberg table in the catalog.

        Args:
            catalog (Catalog): The iceberg catalog.
            schema (ArrowSchema): The table schema.

        Returns:
            IcebergTable: The iceberg table.
        """
        _schema = arrow_schema(self._update_metadata(schema))
        self._update_namespace(catalog)
        try:
            _table = catalog.load_table(self.identifier)
            with _table.update_schema() as update:
                update.union_by_name(_schema)
            self._update_table_partitions(_table)
            self._update_table_properties(_table)
        except NoSuchTableError as _err:
            log.warning(_err)
            _table = catalog.create_table(
                identifier=self.identifier,
                location=self.location,
                schema=_schema,
                properties=self.properties(comments=True))
            self._update_table_partitions(_table)
        return _table

    def _update_namespace(self, catalog: Catalog) -> None:
        """Create the iceberg namespace in the catalog.

        Args:
            catalog (Catalog): The iceberg catalog.
        """
        try:
            log.info("Creating namespace:%s", self.database)
            catalog.create_namespace(
                namespace=self.database,
            )
        except NamespaceAlreadyExistsError as _err:
            log.debug(_err)

    def _update_table_properties(self, table: IcebergTable) -> None:
        """Update the iceberg table in the catalog.

        Args:
            table (IcebergTable): The iceberg table.
        """
        log.info("Updating properties:%s", self.identifier)
        with table.transaction() as transaction:
            for key, value in self.properties(comments=True).items():
                if table.properties.get(key) != value:
                    log.info("Updating property:%s=%s", key, value)
                    transaction.set_properties(**{key: value})
            for key in table.properties.keys():
                if key not in self.properties(comments=True):
                    log.info("Removing property:%s", key)
                    transaction.remove_properties(key)

    def _update_table_partitions(self, table: IcebergTable) -> None:
        """Update the iceberg table partitions in the catalog.

        Args:
            table (IcebergTable): The iceberg table.
        """
        _current_specs = [_ts.name for _ts in table.spec().fields]
        if len(_current_specs) < len(list(self.partition_specs())):
            with table.update_spec() as update:
                for _scn, _tns, _pfn in self.partition_specs():
                    if _pfn not in _current_specs:
                        log.info("Adding partition field: %s", _pfn)
                        update.add_field(
                            source_column_name=_scn,
                            transform=_tns,
                            partition_field_name=_pfn)

    def _update_metadata(self, schema: ArrowSchema) -> Iterator[ArrowField]:
        """Update the iceberg table schema in the catalog.

        Args:
            schema (ArrowSchema): The table schema.

        Yields:
            Iterator[ArrowField]: An iterator of updated fields.
        """
        _title = bytes('doc', 'utf-8')
        for _field in schema:
            try:
                _col = self.schema.find_field(_field.name)
                if _col.doc:
                    _doc = {_title: bytes(_col.doc, 'utf-8')}
                    yield _field.with_metadata(_doc)
                else:
                    yield _field
            except ValueError:
                yield _field

class Job(BaseModel):
    """Dora job class.

    Args:
        name (str): Table asset name.
        sql (str): SQL query to create the job process.
        dialect (str): SQL dialect.
        tables (List[Table]): List of tables used in the job.
    """
    name: str = Field(description="Table asset name")
    sql: str = Field(description="SQL query to create the job process")
    dialect: str = Field(description="SQL dialect", default=DEFAULT_DIALECT)
    tables: List[Table] = Field(description="List of tables used in the job", default=None)

    def model_post_init(self, *args, **kwargs):  # pylint: disable=unused-argument
        """Post init method."""
        self.tables = list(self._parse_script())
        self._check_references()

    def _check_references(self) -> None:
        """Check if all referenced tables are defined."""
        for _table in self.tables:
            for _ref in _table.references:
                _not_found = True
                for _ref_tbl in self.tables:
                    if _ref_tbl.name == f"{_ref.db}_{_ref.name}":
                        _table.ref_locations.append(_ref_tbl.location)
                        _not_found = False
                        break
                if _not_found:
                    raise PydanticCustomError("reference",
                    f"Table '{_ref.db}.{_ref.name}' (ForeignKey) is not in the scope of the job")

    def _parse_script(self) -> Iterator[Table]:
        """
        Parse the SQL script into individual table-specific statements.

        This function processes a SQL script and groups SQL expressions (statements) by their 
        associated tables. It generates tuples containing the table name and the combined SQL 
        statements for that table.

        Yields:
            Iterator[Table]: A generator Dora Table objects.
        """
        _tables = dict()  # Dictionary to group SQL expressions by table names
        # Parse the SQL script using the specified dialect
        for _sql_exp in parse(self.sql, dialect=self.dialect):
            # Extract the table name from the SQL expression
            _table = str(_sql_exp.find(exp.Table))
            # Group SQL expressions by table name
            if _table not in _tables:
                _tables[_table] = dict(dialect=self.dialect, ddl=None, cdl=list())
            # Check the type of SQL expression
            if _sql_exp.find(exp.Create):  # DDL Statement
                _tables[_table]['ddl'] = _sql_exp
            elif _sql_exp.find(exp.Grant):  # CDL Statement
                _tables[_table]['cdl'].append(_sql_exp)
            else:  # Unsupported statement
                raise NotImplementedError(f"Statement type not supported: {_sql_exp.sql()}")

        # Iterate over each table and its associated SQL statements
        for _tbl, _statements in _tables.items():
            log.debug("Table: %s", _tbl)
            # Yield a table object with the combined SQL statements
            yield Table(ast=SQLParser(**_statements))
