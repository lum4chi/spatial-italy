import streamlit as st
from spatial_italy.commons import app_config
from spatial_italy.map import plot_municipalities_map

app_config("Home")

st.markdown("# Spatial Italy")
m = plot_municipalities_map()
m.to_streamlit()
