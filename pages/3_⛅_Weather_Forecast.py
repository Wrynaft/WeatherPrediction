import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from PIL import Image

# Load the future dataframe
future_df = pd.read_csv('weather_forecast.csv', parse_dates=True, index_col=0)

# Filter the dataframe to include only the first 7 days
future_df = future_df.head(10)

# Define a function to map precipitation values to weather condition descriptions and images
def get_weather_condition(precip):
    if precip < 1:
        return "Clear Sky", Image.open("Photos/Clear Sky.png")
    elif precip < 10:
        return "Light Rain", Image.open("Photos/Light Rain.png")
    elif precip < 20:
        return "Moderate Rain", Image.open("Photos/Moderate Rain.png")
    else:
        return "Heavy Rain", Image.open("Photos/Heavy Rain.png")

# Set page configuration
st.set_page_config(page_title="Weather Forecast", page_icon="⛅", layout="wide")

# Create the page title and description
st.title("⛅ Weather Forecast for Kuala Lumpur, Malaysia")
st.write("This page displays the predicted weather conditions for the next 10 days.")
st.write("The current dataset cutoff date is 31-12-2023.")
st.write("""
         ***
         """)

# Create a horizontal table to display the forecast
cols = st.columns(7)

# Iterate over the columns and display the forecast for each day
for col, date in zip(cols, future_df.index):
    with col:
        # Get the predicted precipitation value for the current day
        precip = future_df.loc[date, "predicted_precip"]

        # Get the weather condition description and image based on the precipitation value
        condition, image = get_weather_condition(precip)

        # Display the day of the week
        st.markdown(f"<div style='text-align: center;'>{date.strftime('%A')}</div>", unsafe_allow_html=True)

        # Display the date
        st.markdown(f"<div style='text-align: center;'>{date.strftime('%Y-%m-%d')}</div>", unsafe_allow_html=True)

        # Add an empty line for spacing
        st.markdown("<br>", unsafe_allow_html=True)

        # Display the weather condition image
        st.image(image, use_column_width=True, caption=condition)

        # Display the precipitation value
        st.markdown(f"""
            <div style='text-align: center;'>
                <strong>Precipitation (mm):</strong><br>
                {precip:.2f}
            </div>
        """, unsafe_allow_html=True)
        
# Add a little bit of space before the expander
st.markdown("<br>", unsafe_allow_html=True)

# Create an expander button to display the next 3 days
expander = st.expander("Show next 3 days")

# Create a horizontal table to display the forecast for the next 3 days
next_cols = expander.columns(7)

# Iterate over the columns and display the forecast for each day
for next_col, next_date in zip(next_cols[2:], future_df.index[7:]):
    with next_col:
        # Get the predicted precipitation value for the next day
        next_precip = future_df.loc[next_date, "predicted_precip"]

        # Get the weather condition description and image based on the precipitation value
        next_condition, next_image = get_weather_condition(next_precip)

        # Display the day of the week
        st.markdown(f"<div style='text-align: center;'>{next_date.strftime('%A')}</div>", unsafe_allow_html=True)

        # Display the date
        st.markdown(f"<div style='text-align: center;'>{next_date.strftime('%Y-%m-%d')}</div>", unsafe_allow_html=True)

        # Add an empty line for spacing
        st.markdown("<br>", unsafe_allow_html=True)

        # Display the weather condition image
        st.image(next_image, use_column_width=True, caption=next_condition)

        # Display the precipitation value
        st.markdown(f"""
            <div style='text-align: center;'>
                <strong>Precipitation (mm):</strong><br>
                {next_precip:.2f}
            </div>
        """, unsafe_allow_html=True)
        
# Add a small expandable footer at the end of the web page
footer_expander = st.expander("Disclaimer")
with footer_expander:
    st.write("""
        <div style='text-align: left; font-size: 12px;'>
            ARIMA (AutoRegressive Integrated Moving Average) is used to predict future values of 22 predictor variables for weather forecasting. Please note that, it is well beyond our project scope to accurately predict future values of 22 variables due to the complexity in time-series forecasting and computational time. Nonetheless, this is just an example that highlights our weather prediction model capabilities to generate realistic weather forecasts and target variable ‘precip’ using the input predictor variables.
        </div>
        <br>
    """, unsafe_allow_html=True)