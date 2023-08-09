import pandas as pd
import streamlit as st

from spatial_italy.commons import app_config
from spatial_italy.map import (
    add_custom_layer,
    add_municipality_populations_layer,
    add_seismic_zones_layer,
    create_italy_map,
)

app_config("Home")

# Sidebar
## Available layer selection
LAYERS = ["Population", "Seismic zones"]
st.sidebar.markdown("Select layers to display.")
layers_to_add = st.sidebar.multiselect("Available layers:", LAYERS)

## Custom dataset upload
st.sidebar.divider()
st.sidebar.markdown("Upload a tabular file with at least 2 column.")
st.sidebar.markdown(
    """
    1. municipality keys 
    2. values to be displayed
    """
)
uploaded_file = st.sidebar.file_uploader(
    "Select a file:", type=["csv", "txt", "xlsx"], label_visibility="collapsed"
)
if uploaded_file:
    st.sidebar.divider()
    if uploaded_file.name.split(".")[-1] == "xlsx":
        data = pd.read_excel(uploaded_file)
    else:
        separator = st.sidebar.text_input("Separator", ",", max_chars=1)
        data = pd.read_table(uploaded_file, sep=separator)

    if data.empty or len(data.columns) < 2:
        st.sidebar.warning(
            "You should upload at least 2 column: one for municipality keys and one for value to be displayed. At least one row required."
        )
    else:
        procom_label = st.sidebar.selectbox(
            "Select municipality key column [PRO_COM]:", data.columns, index=0
        )
        value_labels = st.sidebar.multiselect(
            "Select data column:", data.columns.difference([procom_label])
        )
        st.sidebar.dataframe(data)

# Body
st.title("Spatial Italy")
st.markdown(
    "Choose layers or upload your own data. Multiple layers can be choose by the top-right button. Legends can be dragged & dropped."
)
m = create_italy_map()
if layers_to_add and "Population" in layers_to_add:
    add_municipality_populations_layer(m)
if layers_to_add and "Seismic zones" in layers_to_add:
    add_seismic_zones_layer(m)
if uploaded_file and not data.empty and value_labels:
    # TODO Legends for multiple layers are not managed properly,
    # evaluate constraining to 2 layer max.
    for label in value_labels:
        add_custom_layer(m, data, procom_label, label)
m.to_streamlit()
