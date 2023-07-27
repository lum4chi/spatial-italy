import io
import os
import tempfile
import zipfile

import geopandas as gpd
import pandas as pd
import requests
import streamlit as st


def request_population_by_municipalities():
    return pd.read_table(
        "https://demo.istat.it/data/posas/POSAS_2023_it_Comuni.zip",
        compression="zip",
        sep=",",
        encoding="cp1252",
    )


@st.cache_data()
def load_population_by_municipalities():
    df = request_population_by_municipalities()
    # Compute total population by Comune
    df["Popolazione"] = df["Totale maschi"] + df["Totale femmine"]
    df = df.groupby("Comune")["Popolazione"].sum().to_frame().reset_index()
    return df


@st.cache_data()
def load_municipalities_map():
    # EPSG:32632 WGS 84 / UTM zone 32N
    shapes_url = "https://www.istat.it/storage/cartografia/confini_amministrativi/generalizzati/2023/Limiti01012023_g.zip"
    with zipfile.ZipFile(io.BytesIO(requests.get(shapes_url).content)) as zip:
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
