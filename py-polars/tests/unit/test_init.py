import pytest

import polars as pl
from polars.exceptions import ComputeError


def test_init_nonexistent_attribute() -> None:
    with pytest.raises(
        AttributeError, match="module 'polars' has no attribute 'stroopwafel'"
    ):
        pl.stroopwafel


def test_init_exceptions_deprecated() -> None:
    with pytest.deprecated_call(
        match="accessing `ComputeError` from the top-level `polars` module was deprecated in version 1.0.0."
    ):
        exc = pl.ComputeError

    msg = "nope"
    with pytest.raises(ComputeError, match=msg):
        raise exc(msg)


def test_dtype_groups_deprecated() -> None:
    with pytest.deprecated_call(
        match="`INTEGER_DTYPES` was deprecated in version 1.0.0."
    ):
        dtypes = pl.INTEGER_DTYPES

    assert pl.Int8 in dtypes


def test_type_aliases_deprecated() -> None:
    with pytest.deprecated_call(
        match="the `polars.type_aliases` module was deprecated in version 1.0.0."
    ):
        from polars.type_aliases import PolarsDataType
    assert str(PolarsDataType).startswith("typing.Union")


def test_import_all() -> None:
    exec("from polars import *")
