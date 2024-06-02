import streamlit as st
import pandas as pd
import numpy as np

st.write("# How's the Weather? ☀️")

data = pd.read_csv("./actual_cleaned_dataset.csv")
data_temp = data[["datetime", "temp"]]

col1, col2 = st.columns(2)
with col1:
    year = st.selectbox("Year", (2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023))
with col2:
    month = st.selectbox("Month", (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))

display = data.loc[(pd.DatetimeIndex(data["datetime"]).year == year)]
display = display.loc[(pd.DatetimeIndex(display["datetime"]).month == month)]

with st.container(border=True):
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.write("Average temperature:")
        st.write("## " + "{:.2f}".format(display["temp"].mean()) + "°C")
    with col2:
        st.write("No. Rainy Days: ")
        st.write("## " + str(display["rain"].value_counts()[1]))
    with col3:
        st.write("Average rainfall:")
        st.write("## " + "{:.2f}".format(display["precip"].mean()) + "mm")
    with col4:
        st.write("Average humidity: ")
        st.write("## " + "{:.2f}".format(display["humidity"].mean()) + "%")

colA, colB, colC, colD, colE = st.columns(5)
with colA:
    temp = st.checkbox("Temperature")
with colB:
    fl_temp = st.checkbox("Feels-like Temperature")
with colC:
    uv = st.checkbox("UV Index")
with colD:
    precip = st.checkbox("Precipitation")
with colE:
    humidity = st.checkbox("Humidity")

# data['datetime'] = pd.to_datetime(data['datetime'], format='%Y-%m-%d')
# display = data.loc[(data['datetime'].dt.month==year)]
if temp and fl_temp:
    st.subheader("Temperatures")
    st.line_chart(display, x="datetime", y=["temp", "feelslike"])
elif temp:
    st.subheader("Temperatures")
    st.line_chart(display, x="datetime", y="temp")
elif fl_temp:
    st.subheader("Temperatures")
    st.line_chart(display, x="datetime", y="feelslike")

if uv:
    st.subheader("UV Index")
    st.line_chart(display, x="datetime", y="uvindex")

if precip:
    st.subheader("Rainfall intensity (precipitation)")
    st.line_chart(display, x="datetime", y="precip")

if humidity:
    st.subheader("Humidity")
    st.line_chart(display, x="datetime", y="humidity")

# st.subheader('Raw data')
# st.write(display)
