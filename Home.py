import streamlit as st
from spatial_italy.commons import app_config
from spatial_italy.map import create_italy_map, add_municipalities_population

app_config("Home")

st.markdown("# Spatial Italy")
m = create_italy_map()
m = add_municipalities_population(m)
m.to_streamlit()
