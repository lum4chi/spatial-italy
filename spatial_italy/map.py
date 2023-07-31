import pandas as pd
import geopandas as gpd
import pyproj
import plotly.express as px
import json
import leafmap


def make_map_plotly(data: pd.DataFrame, gdf: gpd.GeoDataFrame):
    # Simplify boundaries for a lighter html but also create small gaps between boundaries
    gdf["geometry"] = gdf.simplify(50)
    # In order to use Plotly, a reprojection is needed
    gdf.to_crs(pyproj.CRS.from_epsg(4326), inplace=True)
    # Plotly map
    fig = px.choropleth(
        data,
        geojson=json.loads(gdf.to_json()),
        color="Popolazione",
        hover_name="Comune",
        locations="Comune",
        featureidkey="properties.COMUNE",
        projection="mercator",
    )
    fig.update_geos(fitbounds="locations", visible=False)
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    return fig
