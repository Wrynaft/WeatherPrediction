import streamlit as st
import pandas as pd
import numpy as np

st.write("# How's the Weather? ☀️")

data = pd.read_csv("C:/Users/Ryan Chin/Documents/UM CS/WIE2003 Introduction to Data Science/Assignment/DataApp/actual_cleaned_dataset.csv")

data_temp = data[['datetime', 'temp']]
year = st.selectbox(
    'Year',
    (2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023)
)
month = st.selectbox(
    'Month',
    (1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11,12)
)

temp = st.checkbox("Temperature")
fl_temp = st.checkbox("Feels-like Temperature")
uv = st.checkbox("UV Index")
precip = st.checkbox("Precipitation")
humidity = st.checkbox("Humidity")

# data['datetime'] = pd.to_datetime(data['datetime'], format='%Y-%m-%d')
display = data.loc[(pd.DatetimeIndex(data['datetime']).year==year)]
display = display.loc[(pd.DatetimeIndex(display['datetime']).month==month)]
# display = data.loc[(data['datetime'].dt.month==year)]
if temp and fl_temp:
    st.subheader('Temperatures')
    st.line_chart(display, x="datetime", y=["temp", "feelslike"])
elif temp:
    st.subheader('Temperatures')
    st.line_chart(display, x="datetime", y="temp")
elif fl_temp:
    st.subheader('Temperatures')
    st.line_chart(display, x="datetime", y="feelslike")

if uv:
    st.subheader('UV Index')
    st.line_chart(display, x="datetime", y="uvindex")

if precip:
    st.subheader('Rainfall intensity (precipitation)')
    st.line_chart(display, x="datetime", y="precip")

if humidity:
    st.subheader('Humidity')
    st.line_chart(display, x="datetime", y="humidity")


# st.subheader('Raw data')
# st.write(display)