import pandas as pd
import streamlit as st

st.set_page_config(page_title="Weather Data Viewer ", page_icon="☁️", layout="wide")
st.title("Weather Data Viewer ☁️")
st.write(
    "This page allows you to view weather data of Kuala Lumpur. Please select the **date range** and **features** to display."
)
st.write(
    """
        ***
        """
)

data = pd.read_csv("./actual_cleaned_dataset.csv", parse_dates=["datetime"])

st.subheader("Select date range and features")
start_date = st.date_input(
    "Start Date",
    value=pd.to_datetime("2016-01-01"),
    min_value=pd.to_datetime("2016-01-01"),
    max_value=data["datetime"].max(),
)
end_date = st.date_input(
    "End Date",
    value=data["datetime"].max(),
    min_value=start_date,
    max_value=data["datetime"].max(),
)

mask = (data["datetime"] >= pd.to_datetime(start_date)) & (
    data["datetime"] <= pd.to_datetime(end_date)
)
filtered_data = data.loc[mask]

all_columns = [
    "datetime",
    "temp",
    "feelslike",
    "dew",
    "humidity",
    "precip",
    "precipcover",
    "windgust",
    "windspeed",
    "winddir",
    "sealevelpressure",
    "cloudcover",
    "visibility",
    "uvindex",
    "sunrise",
    "sunset",
    "rain",
    "cloudy",
]
default_columns = [
    "datetime",
    "temp",
    "humidity",
    "precip",
    "precipcover",
    "visibility",
    "uvindex",
    "rain",
    "cloudy",
]
selected_columns = st.multiselect(
    "Select Variables", all_columns, default=default_columns
)

st.write(
    """
        ***
        """
)

# Display data table
st.write(f"Displaying data from {start_date} to {end_date}:")
st.write(
    filtered_data[selected_columns].assign(datetime=lambda x: x["datetime"].dt.date)
)


def convert_df(df):
    return df.to_csv(index=False).encode("utf-8")


csv = convert_df(filtered_data[selected_columns])

st.download_button(
    label="Download data as CSV",
    data=csv,
    file_name="weather_data.csv",
    mime="text/csv",
)
