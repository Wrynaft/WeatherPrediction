import streamlit as st
import pandas as pd
from PIL import Image

future_df = pd.read_csv("weather_forecast.csv", parse_dates=True, index_col=0)

future_df = future_df.head(10)


def get_weather_condition(precip):
    if precip < 1:
        return "Clear Sky", Image.open("Photos/Clear Sky.png")
    elif precip < 10:
        return "Light Rain", Image.open("Photos/Light Rain.png")
    elif precip < 20:
        return "Moderate Rain", Image.open("Photos/Moderate Rain.png")
    else:
        return "Heavy Rain", Image.open("Photos/Heavy Rain.png")


st.set_page_config(page_title="Weather Forecast", page_icon="⛅", layout="wide")

st.title("Weather Forecast for Kuala Lumpur, Malaysia ⛅")
st.write("This page displays the predicted weather conditions for the next 10 days.")
st.write("The current dataset cutoff date is 31-12-2023.")
st.write(
    """
        ***
        """
)

cols = st.columns(7)

for col, date in zip(cols, future_df.index):
    with col:
        precip = future_df.loc[date, "predicted_precip"]

        condition, image = get_weather_condition(precip)

        st.markdown(
            f"<div style='text-align: center;'>{date.strftime('%A')}</div>",
            unsafe_allow_html=True,
        )

        st.markdown(
            f"<div style='text-align: center;'>{date.strftime('%Y-%m-%d')}</div>",
            unsafe_allow_html=True,
        )

        st.markdown("<br>", unsafe_allow_html=True)

        st.image(image, use_column_width=True, caption=condition)

        st.markdown(
            f"""
            <div style='text-align: center;'>
                <strong>Precipitation (mm):</strong><br>
                {precip:.2f}
            </div>
        """,
            unsafe_allow_html=True,
        )

st.markdown("<br>", unsafe_allow_html=True)

expander = st.expander("Show next 3 days")

next_cols = expander.columns(7)

for next_col, next_date in zip(next_cols[2:], future_df.index[7:]):
    with next_col:
        next_precip = future_df.loc[next_date, "predicted_precip"]

        next_condition, next_image = get_weather_condition(next_precip)

        st.markdown(
            f"<div style='text-align: center;'>{next_date.strftime('%A')}</div>",
            unsafe_allow_html=True,
        )

        st.markdown(
            f"<div style='text-align: center;'>{next_date.strftime('%Y-%m-%d')}</div>",
            unsafe_allow_html=True,
        )

        st.markdown("<br>", unsafe_allow_html=True)

        st.image(next_image, use_column_width=True, caption=next_condition)

        st.markdown(
            f"""
            <div style='text-align: center;'>
                <strong>Precipitation (mm):</strong><br>
                {next_precip:.2f}
            </div>
        """,
            unsafe_allow_html=True,
        )

footer_expander = st.expander("Disclaimer")
with footer_expander:
    st.write(
        """
        <div style='text-align: left; font-size: 12px;'>
            ARIMA (AutoRegressive Integrated Moving Average) is used to predict future values of 22 predictor variables for weather forecasting. Please note that, it is well beyond our project scope to accurately predict future values of 22 variables due to the complexity in time-series forecasting and computational time. Nonetheless, this is just an example that highlights our weather prediction model capabilities to generate realistic weather forecasts and target variable ‘precip’ using the input predictor variables.
        </div>
        <br>
    """,
        unsafe_allow_html=True,
    )
