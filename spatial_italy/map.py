import leafmap.foliumap as leafmap
import matplotlib
import numpy as np
import pandas as pd
import streamlit as st

from spatial_italy.data import (
    load_municipalities_frame,
    request_confini_amministrativi_comuni,
    request_zone_sismiche,
)


def create_italy_map() -> leafmap.Map:
    m = leafmap.Map(
        draw_control=False,
        measure_control=False,
        attribution_control=True,
        center=(42.8333, 12.8333),
        zoom=5,
    )
    return m


def add_municipality_populations_layer(
    m: leafmap.Map,
):
    gdf = st.cache_data(load_municipalities_frame)(population=True)
    # Remove unnecessary columns
    data = gdf.assign(Population=gdf.Population.fillna(-1).astype(int)).drop(
        columns="COD_RIP COD_REG COD_PROV COD_CM COD_UTS PRO_COM_T COMUNE CC_UTS Shape_Leng".split()
    )
    # Binning source: https://finanzalocale.interno.gov.it/docum/studi/varie/200707varclass.html#due
    bins = [
        500,
        1000,
        2000,
        3000,
        5000,
        10000,
        20000,
        60000,
        100000,
        250000,
        500000,
        np.inf,
    ]
    # Evenly spaced bins colormap
    blues = matplotlib.colormaps["Blues"]
    blues = blues(np.linspace(0, 1, num=len(bins)))
    blues = [matplotlib.colors.to_hex(color) for color in blues]
    # Map
    m.add_data(
        data,
        column="Population",
        colors=blues,
        legend_title="Population",
        layer_name="Population",
        # scheme="Quantiles",
        # k=10,
        scheme="UserDefined",
        classification_kwds={"bins": bins},
    )


def add_custom_layer(
    m: leafmap.Map,
    df: pd.DataFrame,
    procom_label: str,
    value_label: str,
):
    gdf = st.cache_data(request_confini_amministrativi_comuni)()
    gdf = (
        gdf.set_index("PRO_COM")
        .join(df.set_index(procom_label)[value_label].dropna(), how="right")
        .reset_index()
    )
    m.add_data(
        gdf,
        column=value_label,
        layer_name=value_label,
        scheme="Quantiles",
        cmap="Reds",
    )


def add_seismic_zones_layer(
    m: leafmap.Map,
):
    gdf = st.cache_data(request_zone_sismiche)()
    m.add_data(
        gdf.assign(is_seismic=True),
        column="is_seismic",
        layer_name="Seismic zones",
        colors="ae1d1d",
    )


def add_seismic_municipalities_layer(
    m: leafmap.Map,
):
    gdf = st.cache_data(load_municipalities_frame)(seismic=True)
    # Remove unnecessary rows/columns
    gdf = gdf.dropna(subset="Seismic class")
    data = gdf.drop(
        columns="COD_RIP COD_REG COD_PROV COD_CM COD_UTS PRO_COM_T COMUNE CC_UTS Shape_Leng".split()
    )
    # Scale (dangerous to innocuos)
    map_scale = {
        "1": 0,  # Red
        "1-2A": 1,  # Dark Orange
        "2": 2,  # Orange
        "2A": 3,  # Yellow
        "2A-2B": 4,  # Bright Yellow
        "2B": 5,  # Lime Green
        "2A-3A-3B": 6,  # Yellowish Green
        "2B-3A": 7,  # Greenish Yellow
        "3": 8,  # Green
        "3S": 9,  # Light Green
        "3A": 10,  # Greenish Cyan
        "3A-3B": 11,  # Cyanish Green
        "3B": 12,  # Cyan
        "4": 13,  # Bright Cyan
    }
    data["Seismic class"] = data["Seismic class"].apply(
        lambda cl: f"{map_scale[cl]:2d}. {cl}"
    )
    # Map
    m.add_data(
        data,
        column="Seismic class",
        cmap="autumn",
        # colors=gdf["Seismic class"].map(map_scale),
        legend_title="Seismic class",
        layer_name="Seismic class",
        scheme="UserDefined",
        classification_kwds={"bins": range(0, len(map_scale))},
    )
