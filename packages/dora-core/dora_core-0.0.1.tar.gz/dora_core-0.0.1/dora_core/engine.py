"""Dora engine SQL module.

This module provides functionality to handle SQL operations for the Dora engine.
"""

# pylint: disable=no-member
from abc import ABC, abstractmethod
from typing import Iterator, Callable, List, Tuple, Optional
from enum import Enum
from sqlglot import transpile, Expression, exp
from pydantic import BaseModel, Field
from pyiceberg.catalog import Catalog

from .asset import (
    Table, Job,
    META_COLUMN_DATEF,
    META_COLUMN_FRESH,
    META_COLUMN_FILEN
)

META_COLUMN_UNMAPPED = "Unmapped"

class EngineType(Enum):
    """Engine operation enumeration."""
    ATHENA = "athena"
    DUCKDB = "duckdb"
    SPARK = "spark2"

class Engine(ABC, BaseModel):
    """Dora query engine class.

    Args:
        table (Table): Table object.
        engine (EngineType): Execution engine type.
    """
    
    table: Table = Field(description="Table object")
    engine: EngineType = Field(description="Execution engine type", default=EngineType.DUCKDB)
    raw_columns: Optional[List[str]] = Field(description="Raw columns", default=None)
    cast_columns: Optional[List[str]] = Field(description="Cast columns", default=None)

    def model_post_init(self, *args, **kwargs):  # pylint: disable=unused-argument
        """Post init method."""
        self.raw_columns = list()
        self.cast_columns = list()

    @property
    def raw_view(self) -> exp.Identifier:
        """Temporary raw view name.

        Returns:
            exp.Identifier: The raw view identifier.
        """

    @property
    @abstractmethod
    def raw_table(self) -> exp.Identifier:
        """Temporary raw table name.

        Returns:
            exp.Identifier: The raw table identifier.
        """

    @property
    @abstractmethod
    def cast_table(self) -> exp.Identifier:
        """Cast table name.

        Returns:
            exp.Identifier: The cast table identifier.
        """

    @property
    @abstractmethod
    def test_table(self) -> exp.Identifier:
        """Test table name.

        Returns:
            exp.Identifier: The test table identifier.
        """

    def set_raw_columns(self, raw_columns:List[str]) -> None:
        """Set raw columns method.

        Args:
            raw_columns (List[str]): The raw columns.
        """
        self.raw_columns = list()
        for _col in raw_columns:
            self.raw_columns.append(exp.Identifier(this=_col))

    def set_cast_columns(self, cast_columns:List[str]) -> None:
        """Set raw columns method.

        Args:
            cast_columns (List[str]): The raw columns.
        """
        self.cast_columns = list()
        for _col in cast_columns:
            self.cast_columns.append(exp.Identifier(this=_col))

    def _query_with_placeholders(self) -> Expression:
        """Add a placeholder to the table.

        Returns:
            Expression: The query with placeholders.
        """
        _query = self.table.ast.ddl.expression
        for _source in self.table.ast.get_source():
            for tbl in _query.find_all(exp.Table):
                for __f in tbl.find_all(exp.Literal):
                    if __f.this == _source.this:
                        tbl.replace(exp.Placeholder())
        return _query

    def _cast_columns(self) -> Iterator[Expression]:
        """Cast columns to the correct data type.

        Yields:
            Iterator[Expression]: An iterator of cast expressions.
        """
        if exp.Identifier(this=META_COLUMN_FRESH) not in self.raw_columns:
            yield exp.Alias(
                this=exp.Cast(
                    this=exp.Anonymous(this="now"),
                    to=exp.DataType(this=exp.DataType.Type.TIMESTAMP),
                ),
                alias=exp.Identifier(this=META_COLUMN_FRESH),
            )
        if exp.Identifier(this=META_COLUMN_FILEN) not in self.raw_columns:
            yield exp.Alias(
                this=exp.Placeholder(this="input_file"),
                alias=exp.Identifier(this=META_COLUMN_FILEN),
            )
        if exp.Identifier(this=META_COLUMN_DATEF) not in self.raw_columns:
            yield exp.Alias(
                this=exp.Cast(
                    this=exp.Placeholder(this="input_date"),
                    to=exp.DataType(this=exp.DataType.Type.TIMESTAMP),
                ),
                alias=exp.Identifier(this=META_COLUMN_DATEF),
            )
        col_identifiers = list()
        for _col in self.table.ast.get_columns():
            _col_identifier = _col.find(exp.Identifier)
            col_identifiers.append(_col_identifier)
            yield exp.Alias(
                alias=_col_identifier,
                this=exp.Cast(this=_col_identifier, to=_col.find(exp.DataType)))
        if len(col_identifiers) > 0:
            for raw_column in self.raw_columns:
                if raw_column not in col_identifiers:
                    yield exp.Identifier(this=raw_column)
        else:
            yield exp.Star()

    def read_desc(self) -> str:
        """Desc raw Table.

        Returns:
            str: The transpiled SQL query.
        """
        _sql = exp.Describe(
            this=self.raw_table
        )
        for _query in transpile(sql=_sql.sql(), write=self.engine.value, pretty=True):
            return _query

    def cast_desc(self) -> str:
        """Desc Cast tavke.

        Returns:
            str: The transpiled SQL query.
        """
        _sql = exp.Describe(
            this=self.cast_table
        )
        for _query in transpile(sql=_sql.sql(), write=self.engine.value, pretty=True):
            return _query

    def cast(self, input_file: str = None, input_date: str = None) -> str:
        """Cast query method.

        Args:
            input_file (str, optional): The input file path. Defaults to None.
            input_date (str, optional): The input date. Defaults to None.

        Returns:
            str: The transpiled SQL query.
        """
        _sql = exp.Create(
            this=self.cast_table,
            kind="TABLE",
            exists=True,
            expression=exp.Subquery(
                this=exp.Select(
                    expressions=list(self._cast_columns()),
                ).from_(self.raw_table)
            ),
            properties=exp.Properties(expressions=[exp.TemporaryProperty()]),
        )
        _sql = exp.replace_placeholders(_sql,
               input_file=input_file if input_file is not None else exp.Null(),
               input_date=input_date if input_date is not None else exp.Null())

        for _query in transpile(sql=_sql.sql(), write=self.engine.value, pretty=True):
            return _query

    def unmapped(self) -> str:
        """Unmapped query method.

        Returns:
            str: The transpiled SQL query.
        """
        _unmapped = [col for col in self.raw_columns if col not in self._column_identifiers()]
        if len(_unmapped)>0:
            _sql = exp.Describe(
                this=exp.Subquery(
                    this=exp.Select(
                    expressions=_unmapped,
                    sample=exp.TableSample(
                        size=exp.Literal(this=100, is_string=False)
                    )).from_(self.raw_table)))
            for _query in transpile(sql=_sql.sql(), write=self.engine.value, pretty=True):
                return _query

    def _column_identifiers(self) -> Iterator[exp.Identifier]:
        """Column identifiers.

        Yields:
            Iterator[exp.Identifier]: An iterator of column identifiers.
        """
        for _col in self.table.ast.get_columns():
            yield _col.find(exp.Identifier)

    def test_column_names(self) -> Iterator[str]:
        """Get the test column identifiers."""
        for _test in self._test_checks():
            yield _test.find(exp.Identifier).name
        for _test in self._test_uniques():
            yield _test.find(exp.Identifier).name
        for _test in self._test_nulls():
            yield _test.find(exp.Identifier).name

    def _test_results(self, test_generator: Callable, input_file: str = None) -> Iterator[Tuple[str,Expression]]:
        """Generate test results.

        Args:
            test_generator (Callable): The test generator function.

        Yields:
            Iterator[Expression]: An iterator of test result expressions.
        """
        for _test in test_generator():
            _lit = exp.Literal(this='1', is_string=False)
            _col = _test.find(exp.Identifier)
            _fil = exp.Literal(this='', is_string=True)
            if input_file:
                _fil = exp.Literal(this=input_file, is_string=True)
            yield (_col.name,
                   exp.Select(
                expressions=[
                    exp.Alias(
                        alias=exp.Identifier(this="name"),
                        this=exp.Literal(this=_col.name, is_string=True)
                    ),
                    exp.Alias(
                        alias=exp.Identifier(this="failures"),
                        this=exp.Count(this=_lit)
                    ),
                    exp.Alias(
                        this=exp.NEQ(
                            this=exp.Count(this=_lit),
                            expression=_lit,
                            ),
                        alias=exp.Identifier(this="should_warn"),
                    ),
                    exp.Alias(
                        alias=exp.Identifier(this=META_COLUMN_FILEN),
                        this=_fil,
                    ),
                ],
                where=exp.Where(
                    this=exp.Not(this=_col)
                ),
            ).from_(self.test_table))

    def test_results(self, input_file: str = None) -> Iterator[Tuple[str,str]]:
        """Test query results method.

        Yields:
            Iterator[str]: An iterator of transpiled SQL queries.
        """
        for check in [self._test_checks, self._test_nulls, self._test_uniques]:
            for _name, _test in self._test_results(check, input_file):
                for _query in transpile(sql=_test.sql(), write=self.engine.value):
                    yield (_name, _query)

    def test(self) -> str:
        """Test query method.

        Returns:
            str: The transpiled SQL query.
        """
        _tests = [exp.Star()]
        for _test in self._test_checks():
            _tests.append(_test)
        for _test in self._test_nulls():
            _tests.append(_test)
        for _test in self._test_uniques():
            _tests.append(_test)
        _sql = exp.Create(
            this=self.test_table,
            kind="TABLE",
            exists=True,
            expression=exp.Subquery(
                this=exp.Select(expressions=_tests
                ).from_(
                    exp.Alias(
                    alias=exp.Identifier(this="t0"),
                    this=self.cast_table)
                )
            ),
            properties=exp.Properties(expressions=[exp.TemporaryProperty()]))
        for _query in transpile(sql=_sql.sql(), write=self.engine.value, pretty=True):
            return _query

    def _test_checks(self) -> Iterator[Expression]:
        """Test checks.

        Yields:
            Iterator[Expression]: An iterator of check expressions.
        """
        for _constraint, _check in self.table.ast.get_checks():
            yield exp.Alias(
                alias=_constraint.find(exp.Identifier),
                this=exp.Coalesce(
                    this=exp.Paren(this=_check.this),
                    expressions=[exp.Boolean(this=True)],
                ),
            )

    def _test_nulls(self) -> Iterator[Expression]:
        """Test nulls.

        Yields:
            Iterator[Expression]: An iterator of null test expressions.
        """
        for _col in self.table.ast.get_columns():
            if (_col.find(exp.NotNullColumnConstraint) or
                _col.find(exp.PrimaryKeyColumnConstraint)):
                _col_id = _col.find(exp.Identifier)
                yield exp.Alias(
                    alias=exp.Identifier(this=f"{_col_id.this}_not_null", quoted=False),
                    this=exp.Paren(
                        this=exp.Not(this=exp.Is(this=_col_id, expression=exp.Null()))
                    ),
                )

    def _test_uniques(self) -> Iterator[Expression]:
        """Test unique constraints.

        Yields:
            Iterator[Expression]: An iterator of unique constraint test expressions.
        """
        for idx, _col in enumerate(self.table.ast.get_columns(), start=1):
            if (_col.find(exp.UniqueColumnConstraint) or
                _col.find(exp.PrimaryKeyColumnConstraint)):
                _tbl_id = exp.Identifier(this=f"t{idx}")
                _col_id = _col.find(exp.Identifier)
                _lit_01 = exp.Literal(this="1", is_string=False)
                yield exp.Alias(
                    alias=exp.Identifier(this=f"{_col_id.this}_unique", quoted=False),
                    this=exp.Paren(
                    this=exp.Select(
                    expressions=[
                        exp.Paren(this=exp.Not(
                            this=exp.GT(
                            this=exp.Count(this=exp.Star()),
                            expression=_lit_01))),
                    ],
                    where=exp.Where(
                    this=exp.EQ(
                        this=exp.Column(this=_col_id, table=_tbl_id),
                        expression=exp.Column(
                            this=_col_id,
                            table=exp.Identifier(this="t0")),
                        )
                )
                ).from_(exp.Alias(
                    alias=_tbl_id,
                    this=self.cast_table)
                )))

    def resultset(self) -> str:
        """Results query method.

        Returns:
            str: The transpiled SQL query.
        """
        # Default where clause
        # Return all lines if there are no data quality tests
        _where = exp.Where(
            this=exp.EQ(
                this=exp.Literal(this="1", is_string=False),
                expression=exp.Literal(this="1", is_string=False)))
        # Select all test columns
        _test_list = list(self._filter_cols(self._test_checks, True)) + \
                     list(self._filter_cols(self._test_uniques, True)) + \
                     list(self._filter_cols(self._test_nulls, True))
        # Select all test identifiers
        _test_list_ids = [col.find(exp.Identifier) for col in _test_list]
        # If there are test columns, modify the where clause
        if len(_test_list) > 0:
            _where = self._filter(tests=_test_list, check=True)
        # Create the select statement
        _sql = exp.Select(
            expressions=self.cast_columns,
            from_=self.cast_table,
            where=_where).from_(self.test_table)
        # Transpile the query to the engine dialect
        for _query in transpile(sql=_sql.sql(), write=self.engine.value):
            return _query

    def droped(self, check:str) -> str:
        """Results query method.

        Returns:
            str: The transpiled SQL query.
        """
        # Default where clause
        # Do not return any lines if there are no data quality tests
        _where = exp.Where(
            this=exp.NEQ(
                this=exp.Identifier(this=check),
                expression=exp.true()))
        # Select raw columns 
        _raw_columns = list()
        for _col in self.raw_columns:
            _raw_columns.append(exp.Cast(this=_col,
                                         to=exp.DataType(this=exp.DataType.Type.TEXT)))
        # If there are test columns, modify the where clause
        # Create the select statement
        _sql = exp.Select(
            expressions=_raw_columns,
            from_=self.cast_table,
            where=_where).from_(self.test_table)
        # Transpile the query to the engine dialect
        for _query in transpile(sql=_sql.sql(), write=self.engine.value):
            return _query

    def _filter_cols(self, test_function: Callable, check: bool = True) -> Iterator[exp.Column]:
        """Select all test columns.

        Args:
            test_function (Callable): The test function.
            check (bool, optional): Whether to check the columns. Defaults to True.

        Yields:
            Iterator[exp.Column]: An iterator of test columns.
        """
        for _test in test_function():
            if check:
                yield exp.Column(this=_test.find(exp.Identifier))
            else:
                yield exp.Not(this=exp.Column(this=_test.find(exp.Identifier)))

    def _filter(self, tests: List[exp.Column], ast: Expression = None, check: bool = True) -> Expression:
        """Create the filters for the where clause.

        Args:
            tests (List[exp.Column]): The list of test columns.
            ast (Expression, optional): The abstract syntax tree. Defaults to None.
            check (bool, optional): Whether to check the columns. Defaults to True.

        Returns:
            Expression: The where clause expression.
        """
        try:
            _test = tests.pop()
            if ast is None:
                return self._filter(tests, ast=_test, check=check)
            else:
                if check:
                    return self._filter(tests, ast=exp.And(this=_test, expression=ast), check=check)
                else:
                    return self._filter(tests, ast=exp.Or(this=_test, expression=ast), check=check)
        except IndexError:
            return exp.Where(this=ast)


class Write(Engine):
    """Dora query engine class.

    Args:
        table (Table): Table object.
        engine (EngineType): Execution engine type.
    """
    job: Job = Field(description="Job object")
    replaced: Optional[bool] = Field(description="Replaced flag", default=False)

    def model_post_init(self, *args, **kwargs):  # pylint: disable=unused-argument
        """Post init method."""
        self.replaced = False

    @property
    def raw_view(self) -> exp.Identifier:
        """Temporary raw view name.

        Returns:
            exp.Identifier: The raw view identifier.
        """
        return exp.Identifier(this="__storage__", quote=False)

    @property
    def raw_table(self):
        """Temporary table name.

        Returns:
            exp.Identifier: The temporary table identifier.
        """
        return exp.Identifier(this=f"{self.table.name}_raw", quote=False)

    @property
    def cast_table(self) -> exp.Identifier:
        """Cast table name.

        Returns:
            exp.Identifier: The cast table identifier.
        """
        return exp.Identifier(this=f"{self.table.name}_tmp", quote=False)

    @property
    def test_table(self) -> exp.Identifier:
        """Test table name.

        Returns:
            exp.Identifier: The test table identifier.
        """
        return exp.Identifier(this=f"{self.table.name}_test", quote=False)

    @property
    def stage_table(self) -> exp.Identifier:
        """Test table name.

        Returns:
            exp.Identifier: The test table identifier.
        """
        return exp.Table(this=f"{self.table.table}_stage", db=self.table.database)

    def read(self, catalog:Catalog, input_file:str, input_date:str) -> str:
        """Read query method.

        Args:
            catalog(Catalog): The Iceberg catalog.
            input_file (str): The input file path.
            input_date (str): The input date.

        Returns:
            str: The transpiled SQL query.
        """
        _sql = exp.Create(
            this=self.raw_table,
            kind="TABLE",
            exists=True,
            expression=exp.Select(
                expressions=[exp.Star()],
                where=exp.Where(
                    this=exp.And(
                        this=exp.EQ(
                            this=exp.Identifier(this=META_COLUMN_FILEN),
                            expression=exp.Literal(this=input_file, is_string=True)
                        ),
                        expression=exp.EQ(
                            this=exp.Identifier(this=META_COLUMN_DATEF),
                            expression=exp.Cast(
                                this=exp.Literal(this=input_date, is_string=True),
                                to=exp.DataType(this=exp.DataType.Type.TIMESTAMP),
                            )
                        ),
                    ),
                )
            ).from_(self._query_with_iceberg_scan(catalog)),
            properties=exp.Properties(expressions=[exp.TemporaryProperty()]),
        )
        for _query in transpile(sql=_sql.sql(), write=self.engine.value, pretty=True):
            return _query

    def _query_with_iceberg_scan(self, catalog:Catalog) -> Expression:
        """
        Replace the tables with the Iceber scan reader.

        Returns:
            Expression: The query with placeholders.
        """
        _query = self.table.ast.ddl.expression
        if not self.replaced:
            for exp_tbl in _query.find_all(exp.Table):
                tbl = catalog.load_table(f"{exp_tbl.db}.{exp_tbl.name}")
                exp_tbl.replace(exp.Table(this=exp.Anonymous(
                    this="iceberg_scan",
                    expressions=[exp.Literal(this=tbl.metadata_location, is_string=True)]
                )))
            self.replaced = True
        return _query

    def _foreign_keys(self, source_name:str, target_name:str):
        """Foreign keys method."""
        for _fks in self.table.ast.ddl.find_all(exp.ForeignKey):
            for idx, _fk in enumerate(_fks.expressions):
                yield exp.EQ(
                    this=exp.Column(this=_fk.find(exp.Identifier),
                                    table=exp.Identifier(this=target_name)),
                    expression=exp.Column(
                        this=_fks.find(exp.Reference)\
                                 .find(exp.Schema).expressions[idx]\
                                 .find(exp.Identifier),
                        table=exp.Identifier(this=source_name)),
                )

    def _merge_on(self, source_name:str, target_name:str):
        _fks = list(self._foreign_keys(source_name, target_name))
        if len(_fks) > 1:
            return exp.Paren(
                this=exp.And(this=exp.EQ(
                    this=exp.Literal(this="1", is_string=False),
                    expression=exp.Literal(this="1", is_string=False),
                ),
                expressions=_fks))
        elif len(_fks) == 1:
            return exp.Paren(this=_fks[0])
        else:
            raise ValueError("No foreign keys found")

    def _merge_insert(self, columns: list, source_name: str):
        return exp.Insert(
            this=exp.Tuple(
                expressions=[exp.Column(this=exp.Identifier(this=col)) for col in columns]
            ),
            expression=exp.Tuple(
                expressions=[
                    exp.Column(
                        this=exp.Identifier(this=col),
                        table=exp.Identifier(this=source_name),
                    )
                    for col in columns
                ]
            ),
        )


    def _merge_update(self, columns: list, source_name: str, target_name: str):
        return exp.Update(
            expressions=[
                exp.EQ(
                    this=exp.Column(
                        this=exp.Identifier(this=col),
                        table=exp.Identifier(this=target_name),
                    ),
                    expression=exp.Column(
                        this=exp.Identifier(this=col),
                        table=exp.Identifier(this=source_name),
                    ),
                )
            for col in columns],
        )

    def merge(self, columns_names:list, target_engine:EngineType):
        """Merge query method."""
        _source_alias = "source"
        _target_alias = "target"
        _sql = exp.Merge(
            this=exp.Alias(
                alias=exp.Identifier(this=_target_alias),
                this=exp.Table(this=self.table.table, db=self.table.database)
                ),
            using=exp.Alias(
                alias=exp.Identifier(this=_source_alias),
                this=self.stage_table
            ),
            on=self._merge_on(_source_alias, _target_alias),
            whens=exp.Whens(
                expressions=[
                    exp.When(
                        matched=False,
                        then=self._merge_insert(columns_names, _source_alias)
                    ),
                    exp.When(
                        matched=True,
                        then=self._merge_update(columns_names, _source_alias, _target_alias),
                        condition=exp.GT(
                            this=exp.Column(
                                this=exp.Identifier(this=META_COLUMN_FRESH),
                                table=exp.Identifier(this=_source_alias)
                            ),
                            expression=exp.Column(
                                this=exp.Identifier(this=META_COLUMN_FRESH),
                                table=exp.Identifier(this=_target_alias)
                            )
                        ),
                    )
                ]
            )
        )
        # Transpile the query to the engine dialect
        for _query in transpile(sql=_sql.sql(), write=target_engine.value):
            return _query

class Read(Engine):
    """Dora read engine class."""

    @property
    def raw_view(self) -> exp.Identifier:
        """Temporary raw view name.

        Returns:
            exp.Identifier: The raw view identifier.
        """
        return exp.Identifier(this="__storage__", quote=False)

    @property
    def raw_table(self) -> exp.Identifier:
        """Temporary raw table name.

        Returns:
            exp.Identifier: The raw table identifier.
        """
        return exp.Identifier(this="__raw_data__", quote=False)

    @property
    def cast_table(self) -> exp.Identifier:
        """Cast table name.

        Returns:
            exp.Identifier: The cast table identifier.
        """
        return exp.Identifier(this=f"{self.table.name}_tmp", quote=False)

    @property
    def test_table(self) -> exp.Identifier:
        """Test table name.

        Returns:
            exp.Identifier: The test table identifier.
        """
        return exp.Identifier(this=f"{self.table.name}_test", quote=False)

    def read(self, input_file: str = None) -> str:
        """Read query method.

        Args:
            input_file (str, optional): The input file path. Defaults to None.

        Returns:
            str: The transpiled SQL query.
        """
        _sql = exp.Create(
            this=self.raw_table,
            kind="TABLE",
            exists=True,
            expression=self._query_with_placeholders(),
            properties=exp.Properties(expressions=[exp.TemporaryProperty()]),
        )
        if input_file:
            _sql = exp.replace_placeholders(_sql, input_file)
        for _query in transpile(sql=_sql.sql(), write=self.engine.value, pretty=True):
            return _query
