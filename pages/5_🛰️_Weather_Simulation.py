import streamlit as st
import pandas as pd
import numpy as np
import joblib as joblib
import sklearn

st.title("Weather Simulation 🛰️")
st.write(
    "Simulate your own weather data, and we can predict how intense it will rain! (If it rains)"
)
st.write(
    """
        ***
        """
)

st.subheader("Previous days precipitation")
col1, col2, col3, col4 = st.columns(4)
with col1:
    precip1 = st.number_input("Day 1")
with col2:
    precip2 = st.number_input("Day 2")
with col3:
    precip3 = st.number_input("Day 3")
with col4:
    precip4 = st.number_input("Day 4")

col1, col2, col3 = st.columns(3)
with col1:
    precip5 = st.number_input("Day 5")
with col2:
    precip6 = st.number_input("Day 6")
with col3:
    precip7 = st.number_input("Day 7")

st.subheader("Target day")

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    temp = st.number_input("Temperature", value=28.0)
    sealvlpressure = st.number_input("Sea level pressure: ", value=1015.0)
with col2:
    feelslike = st.number_input("Feels-like", value=28.0)
    visibility = st.number_input("Visibility", value=9.0)
with col3:
    dew = st.number_input("Dew Point", value=24.0)
    precipcover = st.number_input("Precip Cover (%)", min_value=0.0, max_value=100.0)
with col4:
    windgust = st.number_input("Wind Gust", value=20.0)
    cloudcover = st.number_input(
        "Cloud Cover (%)", min_value=0.0, max_value=100.0, value=90.0
    )
with col5:
    windspeed = st.number_input("Wind Speed", value=10.0)
    humidity = st.number_input(
        "Humidity (%)", min_value=0.0, max_value=100.0, value=80.0
    )

col1, col2 = st.columns(2)
with col1:
    winddir = st.slider("Wind Direction", 0, 360)
with col2:
    uv = st.slider("UV index", 0, 10)

if st.button("Predict"):
    df = pd.DataFrame(
        {
            "temp": temp,
            "feelslike": feelslike,
            "dew": dew,
            "humidity": humidity,
            "precipcover": precipcover,
            "windgust": windgust,
            "windspeed": windspeed,
            "winddir": winddir,
            "sealevelpressure": sealvlpressure,
            "cloudcover": cloudcover,
            "visibility": visibility,
            "uvindex": uv,
            "precip_lag_1": np.log1p(precip7),
            "precip_lag_2": np.log1p(precip6),
            "precip_lag_3": np.log1p(precip5),
            "precip_lag_4": np.log1p(precip4),
            "precip_lag_5": np.log1p(precip3),
            "precip_lag_6": np.log1p(precip2),
            "precip_lag_7": np.log1p(precip1),
            "rolling_mean_7": np.mean(
                np.log1p(
                    [precip1, precip2, precip3, precip4, precip5, precip6, precip7]
                )
            ),
            "rolling_std_7": np.std(
                np.log1p(
                    [precip1, precip2, precip3, precip4, precip5, precip6, precip7]
                )
            ),
        },
        index=[0],
    )

    scaler = joblib.load("./scaler.save")
    df_scaled = scaler.transform(df)

    model = joblib.load("./best_rid_reg.pkl")
    prediction = model.predict(df_scaled)

    result = np.expm1(prediction)

    if result < 0:
        st.write("## There is no rain for the day.")
    else:
        st.write("## Rain with " + "{:.2f}".format(result[0]) + "mm")
