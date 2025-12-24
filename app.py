"""
Streamlit application entry point.

Handles:
- User interface
- Visualization
- Integration between modules
"""

import streamlit as st

st.set_page_config(
    page_title="Osaka vs Global Temperature Trends",
    page_icon="🌡️",
    layout="wide",
)

st.title("🌡️ Osaka vs Global Temperature Trends (Annual)")
st.caption(
    "Interactive time-series dashboard: moving average, trend slope (°C/decade), and gap analysis."
)

with st.sidebar:
    st.header("Controls")
    ma_window = st.selectbox("Moving average window (years)", [5, 10, 20], index=1)
    st.divider()
    st.info("Data source will be added next (Berkeley Earth).")

col1, col2, col3 = st.columns(3)
col1.metric("Osaka slope (°C/decade)", "—")
col2.metric("Global slope (°C/decade)", "—")
col3.metric("Osaka − Global (avg)", "—")

st.subheader("Temperature Trends")
st.warning("Next step: load dataset and render chart.")