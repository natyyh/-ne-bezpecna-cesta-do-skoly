import streamlit as st
dt = {"latitude": [49.60470], "longtitude":[17.24184]}
st.map(dt, latitude="latitude", longitude="longtitude", zoom=10)



