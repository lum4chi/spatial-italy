import leafmap.foliumap as leafmap

from spatial_italy.data import load_municipalities_map


def plot_municipalities_map():
    gdf = load_municipalities_map(population=True)
    # Map
    m = leafmap.Map()
    # Remove unnecessary columns
    data = gdf.assign(Population=gdf.Population.fillna(-1).astype(int)).drop(
        columns="COD_RIP COD_REG COD_PROV COD_CM COD_UTS PRO_COM_T COMUNE CC_UTS Shape_Leng".split()
    )
    m.add_data(
        data,
        column="Population",
        scheme="Quantiles",
        cmap="Blues",
        legend_title="Population",
        layer_name="Population",
    )
    return m
