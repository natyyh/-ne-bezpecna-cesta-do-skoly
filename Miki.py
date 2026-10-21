import streamlit as st
dt = {"latitude": [48.8567], "longitude": [2.2970]}
st.map(dt, latitude="latitude", longitude="longitude", zoom=10)