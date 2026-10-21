import streamlit as st
dt={"latitude": [49.8433056,50.1256267], "longitude": [15.9961606, 17.3842747]}
st.map(dt, latitude="latitude", longitude="longitude", zoom=30)