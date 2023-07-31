import streamlit as st


def app_config(title: str):
    """Setup page & session state. Must be the first script instruction called."""
    st.set_page_config(
        page_title=f"Spatial Italy • {title}",
        page_icon="🇮🇹",
        layout="wide",
        initial_sidebar_state="expanded",
    )
