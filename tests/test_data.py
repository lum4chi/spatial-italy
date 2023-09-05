import geopandas as gpd
import pandas as pd

from spatial_italy.data import (
    load_population_by_municipalities,
    request_confini_amministrativi_comuni,
    add_bilingual_full_municipality_name,
    request_POSAS_2023_it_Comuni,
    add_municipality_populations,
    add_seismic_municipalities,
    load_municipalities_frame,
    request_zone_sismiche,
    request_comuni_sismici,
)
from .fixtures.demografia import POSAS_2023_it_Comuni_sample
from .fixtures.geografia import classificazione_sismica_comuni
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


def test_add_bilingual_full_municipality_name(
    mocker, confini_amministrativi_comuni_sample
):
    mocker.patch(
        "spatial_italy.data.request_confini_amministrativi_comuni",
        return_value=confini_amministrativi_comuni_sample,
    )
    gdf = request_confini_amministrativi_comuni()
    gdf = add_bilingual_full_municipality_name(gdf)
    assert isinstance(gdf, gpd.GeoDataFrame)
    assert all(gdf.loc[gdf.COMUNE == "Vandoies", "COMUNE_A"] == "Vandoies / Vintl")


def test_add_municipality_populations(
    mocker, confini_amministrativi_comuni_sample, POSAS_2023_it_Comuni_sample
):
    mocker.patch(
        "spatial_italy.data.request_confini_amministrativi_comuni",
        return_value=confini_amministrativi_comuni_sample,
    )
    mocker.patch(
        "spatial_italy.data.request_POSAS_2023_it_Comuni",
        return_value=POSAS_2023_it_Comuni_sample,
    )
    gdf = request_confini_amministrativi_comuni()
    gdf = add_municipality_populations(gdf)
    assert isinstance(gdf, gpd.GeoDataFrame)
    assert "Population" in gdf.columns


def test_add_seismic_municipalities(
    mocker, confini_amministrativi_comuni_sample, classificazione_sismica_comuni
):
    mocker.patch(
        "spatial_italy.data.request_confini_amministrativi_comuni",
        return_value=confini_amministrativi_comuni_sample,
    )
    mocker.patch(
        "spatial_italy.data.request_zone_sismiche",
        return_value=classificazione_sismica_comuni,
    )
    gdf = request_confini_amministrativi_comuni()
    gdf = add_seismic_municipalities(gdf)
    assert isinstance(gdf, gpd.GeoDataFrame)
    assert "Seismic class" in gdf.columns


def test_load_municipalities_frame(
    mocker,
    confini_amministrativi_comuni_sample,
    POSAS_2023_it_Comuni_sample,
    classificazione_sismica_comuni,
):
    mocker.patch(
        "spatial_italy.data.request_confini_amministrativi_comuni",
        return_value=confini_amministrativi_comuni_sample,
    )
    mocker.patch(
        "spatial_italy.data.request_POSAS_2023_it_Comuni",
        return_value=POSAS_2023_it_Comuni_sample,
    )
    mocker.patch(
        "spatial_italy.data.request_zone_sismiche",
        return_value=classificazione_sismica_comuni,
    )

    gdf = load_municipalities_frame()
    assert isinstance(gdf, gpd.GeoDataFrame)

    gdf = load_municipalities_frame(population=True)
    assert "Population" in gdf.columns

    gdf = load_municipalities_frame(seismic=True)
    assert "Seismic class" in gdf.columns


def test_request_zone_sismiche():
    assert isinstance(request_zone_sismiche(), gpd.GeoDataFrame)
