import geopandas as gpd
import pandas as pd

from spatial_italy.data import (
    load_population_by_municipalities,
    request_confini_amministrativi_comuni,
    request_POSAS_2023_it_Comuni,
    load_municipalities_frame,
)
from .fixtures.demografia import POSAS_2023_it_Comuni_sample
from .fixtures.confini import confini_amministrativi_comuni_sample


def test_request_POSAS_2023_it_Comuni():
    assert isinstance(request_POSAS_2023_it_Comuni(), pd.DataFrame)


def test_load_population_by_municipalities(mocker, POSAS_2023_it_Comuni_sample):
    mocker.patch(
        "spatial_italy.data.request_POSAS_2023_it_Comuni",
        return_value=POSAS_2023_it_Comuni_sample,
    )
    df = load_population_by_municipalities()
    assert isinstance(df, pd.DataFrame)


def test_request_confini_amministrativi_comuni():
    assert isinstance(request_confini_amministrativi_comuni(), gpd.GeoDataFrame)


def test_load_municipalities_frame(mocker, confini_amministrativi_comuni_sample):
    mocker.patch(
        "spatial_italy.data.request_confini_amministrativi_comuni",
        return_value=confini_amministrativi_comuni_sample,
    )
    gdf = load_municipalities_frame()
    assert isinstance(gdf, gpd.GeoDataFrame)
    assert all(gdf.loc[gdf.COMUNE == "Vandoies", "COMUNE_A"] == "Vandoies / Vintl")

    gdf = load_municipalities_frame(population=True)
    assert "Population" in gdf.columns
