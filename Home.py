import streamlit as st
from spatial_italy.data import (
    load_population_by_municipalities,
    load_municipalities_map,
)
from spatial_italy.map import make_map

st.markdown("# Spatial Italy")

df = load_population_by_municipalities()
gdf = load_municipalities_map()
fig = make_map(df, gdf)

st.plotly_chart(fig, use_container_width=True)
