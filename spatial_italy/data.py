import io
import os
import tempfile
import zipfile

import geopandas as gpd
import pandas as pd
import requests


def request_POSAS_2023_it_Comuni() -> pd.DataFrame:
    return pd.read_table(
        "https://demo.istat.it/data/posas/POSAS_2023_it_Comuni.zip",
        compression="zip",
        sep=",",
        encoding="cp1252",
    )


def load_population_by_municipalities():
    df = request_POSAS_2023_it_Comuni()
    # Compute total population by Comune
    df["Population"] = df["Totale maschi"] + df["Totale femmine"]
    df = (
        df.groupby(["Codice comune", "Comune"])["Population"]
        .sum()
        .to_frame()
        .reset_index()
    )
    return df


def request_confini_amministrativi_comuni() -> gpd.GeoDataFrame:
    # EPSG:32632 WGS 84 / UTM zone 32N
    url = "https://www.istat.it/storage/cartografia/confini_amministrativi/generalizzati/2023/Limiti01012023_g.zip"
    with zipfile.ZipFile(io.BytesIO(requests.get(url).content)) as zip:
        with tempfile.TemporaryDirectory() as tempdir:
            zip.extractall(tempdir)
            gdf = gpd.read_file(
                os.path.join(
                    tempdir, "Limiti01012023_g/Com01012023_g/Com01012023_g_WGS84.shp"
                ),
                encoding="UTF-8",
            )
    gdf.crs = "epsg:32632"
    return gdf


def add_bilingual_full_municipality_name(gdf: gpd.GeoDataFrame):
    # Compute full name for bilingual municipalities
    gdf["COMUNE_A"] = gdf[["COMUNE", "COMUNE_A"]].apply(
        lambda r: " / ".join(r.dropna()), axis=1
    )
    return gdf


def add_municipality_populations(gdf: gpd.GeoDataFrame):
    df = load_population_by_municipalities()
    gdf = (
        gdf.set_index("PRO_COM")
        .join(df.set_index("Codice comune").Population)
        .reset_index()
    )
    return gdf


def load_municipalities_frame(population: bool = False):
    gdf = request_confini_amministrativi_comuni()
    gdf = add_bilingual_full_municipality_name(gdf)
    if population:
        gdf = add_municipality_populations(gdf)
    return gdf


def request_zone_sismiche():
    # Source: http://zonesismiche.mi.ingv.it/documenti/App2.pdf
    url = "http://zonesismiche.mi.ingv.it/elaborazioni/dati_di_ingresso/ZS9.ZIP"
    with zipfile.ZipFile(io.BytesIO(requests.get(url).content)) as zip:
        with tempfile.TemporaryDirectory() as tempdir:
            zip.extractall(tempdir)
            gdf = gpd.read_file(
                os.path.join(tempdir, "zs9.shp"),
                encoding="UTF-8",
            )
    gdf.crs = "epsg:4326"
    return gdf
