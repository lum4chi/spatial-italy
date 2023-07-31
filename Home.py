import streamlit as st
from spatial_italy.commons import app_config
from spatial_italy.data import (
    load_population_by_municipalities,
    load_municipalities_map,
)
from spatial_italy.map import make_map_plotly

app_config("Home")

st.markdown("# Spatial Italy")

df = load_population_by_municipalities()
gdf = load_municipalities_map()
fig = make_map_plotly(df, gdf)

st.plotly_chart(fig, use_container_width=True)
