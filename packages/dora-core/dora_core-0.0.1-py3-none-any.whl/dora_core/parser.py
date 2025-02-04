"""Dora Parser module.

This module provides functionality to parse and analyze SQL statements.
"""

# pylint: disable=no-member

from typing import Iterator, Tuple, List
from re import match

from pydantic import BaseModel, Field, ConfigDict
from sqlglot import Expression, parse, expressions, transpile
from pyiceberg.types import (
    PrimitiveType,
    BooleanType,
    IntegerType,
    StringType,
    FloatType,
    TimeType,
    TimestampType,
    TimestamptzType,
    UUIDType,
    DoubleType,
    DateType,
    DecimalType)
from pyiceberg.transforms import (
    Transform,
    YearTransform,
    MonthTransform,
    DayTransform,
    HourTransform,
    BucketTransform,
    TruncateTransform,
    IdentityTransform)

from .utils import logger

log = logger(__name__)

class SQLParser(BaseModel):
    """SQL Parser class.

    Args:
        dialect (str): SQL dialect.
        ddl (Expression): DDL expression.
        cdl (List[Expression]): CDL expression.
    """
    dialect: str = Field(description="SQL dialect", exclude=True)
    ddl: Expression = Field(description="DDL expression", exclude=True)
    cdl: List[Expression] = Field(description="CDL expression", default=None, exclude=True)

    model_config = ConfigDict(arbitrary_types_allowed=True)

    def _validate(self):
        """
        Validates the SQL statement to ensure it is a valid CREATE TABLE statement.
        """
        if self.ddl.find(expressions.Create) is None:
            raise ValueError(f"Not a CREATE TABLE statement: {self.ddl.sql()}")
        if self.ddl.find(expressions.Table) is None:
            raise ValueError(f"Not a CREATE TABLE statement: {self.ddl.sql()}")
        if self.ddl.find(expressions.Subquery | expressions.Query).find(expressions.Select) is None:
            raise ValueError(f"Cant find a SELECT statement in: {self.ddl.sql()}")

    def get_foreign_key(self) -> Iterator[expressions.Table]:
        """
        Extracts foreign key expressions from a SQL expression.

        Yields:
            Iterator[expressions.Table]: An iterator of foreign key expressions.
        """
        for _fk in self.ddl.find_all(expressions.ForeignKey):
            yield _fk.find(expressions.Table)

    def get_query(self, dialect: str) -> str:
        """
        Extract the query from a SQL expression.

        Args:
            dialect (str): The SQL dialect to which the query should be transpiled.

        Returns:
            str: The transpiled SQL query.
        """
        return transpile(sql=self.ddl.expression.sql(), read=self.dialect, write=dialect, pretty=True)

    def get_columns(self) -> Iterator[expressions.ColumnDef]:
        """
        Extracts column definitions from a SQL expression.

        Yields:
            Iterator[expressions.ColumnDef]: An iterator of column definitions.
        """
        _schema_expression = self.ddl.find(expressions.Schema)
        if _schema_expression is not None:
            for _schema in _schema_expression:
                if isinstance(_schema, expressions.ColumnDef):
                    yield _schema

    def get_partitions(self) -> Iterator[expressions.Anonymous]:
        """
        Extracts partition definitions from a SQL expression.

        Yields:
            Iterator[expressions.Anonymous]: An iterator of partition definitions.
        """
        _properties = self.ddl.find(expressions.Properties)
        for _partitions in _properties.expressions:
            if isinstance(_partitions, expressions.PartitionedByProperty):
                for __partition in _partitions.this.expressions:
                    yield __partition

    def get_location(self) -> Iterator[expressions.LocationProperty]:
        """
        Extracts the location from a SQL expression.

        Yields:
            Iterator[expressions.LocationProperty]: An iterator of location properties.
        """
        _properties = self.ddl.find(expressions.Properties)
        _location = _properties.find(expressions.LocationProperty)
        if isinstance(_location, expressions.LocationProperty):
            yield _location.find(expressions.Literal)

    def get_table(self) -> str:
        """
        Extracts the table name from a SQL expression.

        Returns:
            str: The table name.
        """
        return self.ddl.find(expressions.Table)

    def get_properties(self) -> Iterator[expressions.Property]:
        """
        Extracts properties from a SQL expression.

        Yields:
            Iterator[expressions.Property]: An iterator of properties.
        """
        _properties = self.ddl.find(expressions.Properties)
        for _property in _properties.find_all(expressions.Property):
            if _property.__class__ == expressions.Property:
                yield _property

    def get_description(self) -> Iterator[expressions.SchemaCommentProperty]:
        """
        Extracts the description from a SQL expression.

        Yields:
            Iterator[expressions.SchemaCommentProperty]: An iterator of schema comment properties.
        """
        _properties = self.ddl.find(expressions.Properties)
        _comment = _properties.find(expressions.SchemaCommentProperty)
        if isinstance(_comment, expressions.SchemaCommentProperty):
            yield _comment.find(expressions.Literal)

    def get_constraints(self) -> Iterator[expressions.Constraint]:
        """
        Extracts constraint expressions from a SQL expression.

        Yields:
            Iterator[expressions.Constraint]: An iterator of constraints.
        """
        _schema_expression = self.ddl.find(expressions.Schema)
        if _schema_expression is not None:
            for _scm in _schema_expression:
                if isinstance(_scm, expressions.Constraint):
                    yield _scm

    def get_unique(self) -> Iterator[expressions.UniqueColumnConstraint]:
        """
        Extracts unique constraints from a SQL expression.

        Yields:
            Iterator[expressions.UniqueColumnConstraint]: An iterator of unique constraints.
        """
        for _constraint in self.get_constraints():
            for _unique in _constraint.expressions:
                if isinstance(_unique, expressions.UniqueColumnConstraint):
                    yield _unique

    def get_checks(self) -> Iterator[Tuple[expressions.Constraint, expressions.CheckColumnConstraint]]:
        """
        Extracts check constraints from a SQL expression.

        Yields:
            Iterator[Tuple[expressions.Constraint, expressions.CheckColumnConstraint]]: An iterator of check constraints.
        """
        for _constraint in self.get_constraints():
            for _check in _constraint.expressions:
                if isinstance(_check, expressions.CheckColumnConstraint):
                    yield (_constraint, _check)


    @staticmethod
    def _check_protocol(value:str) -> bool:
        protocols = ['s3', 'az', 'abfss', 'gs']
        if value.startswith(tuple(f"{_protocol}://" for _protocol in protocols)):
            return True
        if "://" in value:
            raise NotImplementedError(f"Invalid path: {value}. Supported protocols: {protocols}")
        return False


    def _get_sources(self, sql:expressions.Expression) -> Iterator[expressions.Anonymous]:
        """
        Extracts the source expression from a SQL expression.

        Yields:
            Iterator[expressions.Anonymous]: An iterator of Anonymous funtions.
        """
        for _table in sql.find_all(expressions.Table):
            _name = _table.find(expressions.Identifier)
            if _name is not None:
                if self._check_protocol(_name.this):
                    if _name.this.endswith(
                        tuple(_fmt for _fmt in ['.csv', '.csv.gz', '.csv.zip'])):
                        yield expressions.Anonymous(
                            this='read_csv',
                            expressions=[
                                expressions.Literal(this=_name.this),
                                expressions.EQ(
                                    this=expressions.Identifier(this='header'),
                                    expression=expressions.Boolean(this=True))])
                    if _name.this.endswith(
                        tuple(_fmt for _fmt in ['.json', '.json.gz', '.json.zip'])):
                        yield expressions.Anonymous(
                            this='read_json',
                            expressions=[expressions.Literal(this=_name.this)])
                    if _name.this.endswith(
                        tuple(_fmt for _fmt in ['.parquet', '.snappy.parquet'])):
                        yield expressions.Anonymous(
                            this='read_parquet',
                            expressions=[expressions.Literal(this=_name.this)])
            if isinstance(_table.this, expressions.ReadCSV):
                yield expressions.Anonymous(
                    this='read_csv',
                    expressions=[_table.this.find(expressions.Literal)] + _table.this.expressions
                )
            if isinstance(_table.this, expressions.Anonymous):
                if _table.this.this in ['read_csv', 'read_json', 'read_parquet']:
                    yield _table.this

    def get_source(self) -> Iterator[expressions.Literal]:
        """
        Extracts the source expression from a SQL expression.

        Yields:
            Iterator[expressions.Literal]: An iterator of source literals.
        """
        for _from in self.ddl.find(expressions.Subquery | expressions.Query).find_all(expressions.From):
            for _source in self._get_sources(_from):
                yield _source.find(expressions.Literal)

    def _ddl_statements(self, sql: str) -> Expression:
        """
        Parses a SQL string into a list of CREATE TABLE and GRANT expressions.

        Args:
            sql (str): The SQL string to be parsed.

        Returns:
            Expression: The CREATE TABLE expression.
        """
        for _p_exp in parse(sql, dialect=self.dialect):
            if isinstance(_p_exp, expressions.Create):
                if _p_exp.kind == 'TABLE':
                    return _p_exp
                else:
                    raise NotImplementedError(f'Unsupported CREATE type: {_p_exp.kind}')

    def _cdl_statements(self, sql: str) -> Iterator[Expression]:
        """
        Parses a SQL string into a list of CREATE TABLE and GRANT expressions.

        Args:
            sql (str): The SQL string to be parsed.

        Yields:
            Iterator[Expression]: An iterator of GRANT expressions.
        """
        for _p_exp in parse(sql, dialect=self.dialect):
            if isinstance(_p_exp, expressions.Grant):
                if _p_exp.args['kind'] != 'TABLE':
                    log.error('Only GRANT TABLE is supported. Found: %s', _p_exp.args["kind"])
                    raise NotImplementedError(f'Unsupported GRANT type: {_p_exp.args["kind"]}')
                _grant_tbl = _p_exp.find(expressions.Table)
                if _grant_tbl != self.get_table():
                    _msg = 'grant table "%s" is different from "%s"'
                    log.error(_msg, _grant_tbl, self.get_table())
                    _err = f'GRANT TABLE does not match CREATE TABLE: {_grant_tbl}'
                    raise ValueError(_err)
                yield _p_exp

    @staticmethod
    def column_required(col: Expression) -> bool:
        """
        Checks if a column is required.

        Args:
            col (Expression): The column expression.

        Returns:
            bool: True if the column is required, False otherwise.
        """
        if isinstance(col.constraints, list):
            for constraint in col.constraints:
                if isinstance(constraint, expressions.ColumnConstraint):
                    if isinstance(constraint.kind, expressions.NotNullColumnConstraint):
                        return True
                    if isinstance(constraint.kind, expressions.PrimaryKeyColumnConstraint):
                        return True
        return False

    @staticmethod
    def column_comment(col: Expression) -> str:
        """
        Extracts the comment from a column.

        Args:
            col (Expression): The column expression.

        Returns:
            str: The column comment.
        """
        if isinstance(col.constraints, list):
            for constraint in col.constraints:
                if isinstance(constraint, expressions.ColumnConstraint):
                    if isinstance(constraint.kind, expressions.CommentColumnConstraint):
                        return constraint.kind.this.this
        return str()

    @staticmethod
    def column_type(column: expressions.ColumnDef) -> PrimitiveType:
        """
        Map SQL types to Iceberg PrimitiveType.

        Args:
            column (expressions.ColumnDef): The column definition.

        Returns:
            PrimitiveType: The corresponding Iceberg PrimitiveType.
        """
        # Boolean Type
        if column.kind.sql() == "BOOLEAN":
            return BooleanType()
        if column.kind.sql() == "BOOL":
            return BooleanType()
        # Integer Types
        if column.kind.sql() == "INTEGER":
            return IntegerType()
        if column.kind.sql() == "INT":
            return IntegerType()
        # Floating-Point Types
        if column.kind.sql() == "FLOAT":
            return FloatType()
        if column.kind.sql() == "REAL":
            return DoubleType()
        if column.kind.sql() == "DOUBLE":
            return DoubleType()
        # Fixed-Point Decimals (Precision, Scale)
        if column.kind.sql().startswith("DECIMAL"):
            return DecimalType(*[int(exp.this.this) for exp in column.kind.expressions])
        if column.kind.sql().startswith("NUMERIC"):
            return DecimalType(*[int(exp.this.this) for exp in column.kind.expressions])
        # Text Types
        if column.kind.sql() == "STRING":
            return StringType()
        if column.kind.sql() == "VARCHAR":
            return StringType()
        if column.kind.sql() == "TEXT":
            return StringType()
        # Time Types
        if column.kind.sql() == "TIME":
            return TimeType()
        # Timestamp Types
        if column.kind.sql() == "TIMESTAMPTZ":
            return TimestamptzType()
        if column.kind.sql() == "TIMESTAMP":
            return TimestampType()
        if column.kind.sql() == "DATETIME":
            return TimestampType()
        # Date Types
        if column.kind.sql() == "DATE":
            return DateType()
        # Universally Unique Identifiers
        if column.kind.sql() == "UUID":
            return UUIDType()
        if column.kind.sql() == "STRUCT":
            return StringType()
        raise NotImplementedError(column.kind)

    @staticmethod
    def partition_transform(exp: expressions.Anonymous) -> Transform:
        """
        Extracts the partition transform from a SQL expression.

        Args:
            exp (expressions.Anonymous): The partition expression.

        Returns:
            Transform: The corresponding partition transform.
        """
        # partition by year
        if str(exp.this).lower() == "years":
            return YearTransform()
        if isinstance(exp, expressions.Year):
            return YearTransform()
        # partition by month
        if str(exp.this).lower() == "months":
            return MonthTransform()
        if isinstance(exp, expressions.Month):
            return MonthTransform()
        # equivalent to dateint partitioning
        if str(exp.this).lower() == "days":
            return DayTransform()
        if isinstance(exp, expressions.Day):
            return DayTransform()
        # equivalent to dateint and hour partitioning
        if str(exp.this).lower() == "hour":
            return HourTransform()
        if str(exp.this).lower() == "hours":
            return HourTransform()
        if str(exp.this).lower() == "date_hour":
            return HourTransform()
        # partition by hashed value mod N buckets
        if str(exp.this).lower() == "bucket":
            _buckets = int(exp.find(expressions.Literal).this)
            return BucketTransform(num_buckets=_buckets)
        # partition by hashed value mod N buckets
        if str(exp.this).lower() == "truncate":
            _width = int(exp.find(expressions.Literal).this)
            return TruncateTransform(width=_width)
        if isinstance(exp, expressions.Identifier):
            return IdentityTransform()
