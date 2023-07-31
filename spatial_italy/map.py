import leafmap.foliumap as leafmap
import numpy as np
import matplotlib
from spatial_italy.data import load_municipalities_map


def plot_municipalities_map():
    gdf = load_municipalities_map(population=True)
    # Map
    m = leafmap.Map()
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
