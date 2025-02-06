import pytest
import pandas as pd
from ..omnip import (
    _check_if_liana,
    get_progeny,
    get_resource,
    show_resources,
    get_dorothea,
    get_collectri,
    get_ksn_omnipath
)


def test_check_if_liana():
    _check_if_liana()


def test_get_resource():
    res = get_resource('TFcensus')
    assert type(res) is pd.DataFrame
    assert res.shape[0] > 0


def test_show_resources():
    lst = show_resources()
    assert type(lst) is list
    assert len(lst) > 0


def test_get_dorothea():
    df = get_dorothea(organism='human')
    assert type(df) is pd.DataFrame
    assert df.shape[0] > 0
    with pytest.raises(ValueError):
        get_dorothea(organism='asdfgh')
    get_dorothea(organism='mouse')


def test_get_collectri():
    df = get_collectri(organism='human', split_complexes=False)
    assert type(df) is pd.DataFrame
    assert df.shape[0] > 0
    with pytest.raises(ValueError):
        get_collectri(organism='asdfgh', split_complexes=False)
    get_collectri(organism='mouse', split_complexes=False)
    subunits_df = get_collectri(organism='human', split_complexes=True)


def test_get_progeny():
    df = get_progeny(organism='human', top=100)
    n_paths = len(df['source'].unique())
    n_rows = (n_paths * 100)
    assert type(df) is pd.DataFrame
    assert df.shape[0] == n_rows
    with pytest.raises(ValueError):
        get_progeny(organism='asdfgh')


def test_get_ksn_omnipath():
    df = get_ksn_omnipath()
    assert type(df) is pd.DataFrame
    assert df.shape[0] > 0
