import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from PIL import Image

# Load the future dataframe
future_df = pd.read_csv('weather_forecast.csv', parse_dates=True, index_col=0)

# Filter the dataframe to include only the first 7 days
future_df = future_df.head(7)

# Define a function to map precipitation values to weather condition descriptions and images
def get_weather_condition(precip):
    if precip == 0:
        return "Clear Sky", Image.open("Photos/Clear Sky.png")
    elif precip < 10:
        return "Light Rain", Image.open("Photos/Light Rain.jpg")
    elif precip < 20:
        return "Moderate Rain", Image.open("Photos/Moderate Rain.png")
    else:
        return "Heavy Rain", Image.open("Photos/Heavy Rain.jpeg")

# Set page configuration
st.set_page_config(page_title="Weather Forecast", page_icon="🌤️", layout="wide")

# Create the page title and description
st.title("⛅ Weather Forecast for Kuala Lumpur, Malaysia")
st.write("This page displays the predicted weather conditions for the next 7 days.")
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
        st.write(date.strftime("%A"))

        # Display the date
        st.write(date.strftime("%Y-%m-%d"))

        # Display the weather condition image
        st.image(image, use_column_width=True)

        # Display the precipitation value
        st.metric(label="Precipitation (mm)", value=f"{precip:.2f}")