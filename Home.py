import traceback

import pandas as pd
import streamlit as st

from spatial_italy.commons import app_config
from spatial_italy.map import (
    add_custom_layer,
    add_municipality_populations_layer,
    create_italy_map,
)

app_config("Home")

# Sidebar
## Available layer selection
LAYERS = ["Population"]
st.sidebar.markdown("Select layers to display.")
layers_to_add = st.sidebar.multiselect("Available layers:", LAYERS)

## Custom dataset upload
st.sidebar.divider()
st.sidebar.markdown(
    """Upload a tabular file with at least 2 column.

    1. municipality keys
    2. values to be displayed
    """
)
uploaded_file = st.sidebar.file_uploader("", type=["csv", "txt", "xlsx"])
st.sidebar.divider()
if uploaded_file:
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
        value_label = st.sidebar.selectbox(
            "Select data column:", ["-"] + data.columns.to_list(), index=0
        )
        st.sidebar.dataframe(data)

# Body
st.title("Spatial Italy")
st.markdown(
    "Choose layers or upload your own data. Multiple layers can be choose by the top-right button. Legends can be dragged & dropped."
)
m = create_italy_map()
if layers_to_add and "Population" in layers_to_add:
    m = add_municipality_populations_layer(m)
if uploaded_file and not data.empty and value_label != "-":
    m = add_custom_layer(m, data, procom_label, value_label)
m.to_streamlit()
