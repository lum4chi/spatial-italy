import pandas as pd

from spatial_italy.data import load_population_by_municipalities


def test_load_population_by_municipalities():
    df = load_population_by_municipalities()
    assert isinstance(df, pd.DataFrame)
