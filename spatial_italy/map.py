import geopandas as gdp
import leafmap.foliumap as leafmap
import matplotlib
import numpy as np
import pandas as pd

from spatial_italy.data import (
    load_municipalities_frame,
    request_confini_amministrativi_comuni,
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


def add_municipality_populations_layer(m: leafmap.Map):
    gdf = load_municipalities_frame(population=True)
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
    return m


def add_custom_layer(
    m: leafmap.Map, df: pd.DataFrame, procom_label: str, value_label: str
):
    gdf = request_confini_amministrativi_comuni()
    gdf = (
        gdf.set_index("PRO_COM")
        .join(df.set_index(procom_label)[value_label], how="right")
        .reset_index()
    )
    m.add_data(
        gdf,
        column=value_label,
        layer_name=value_label,
        scheme="Quantiles",
        cmap="Reds",
    )
    return m
