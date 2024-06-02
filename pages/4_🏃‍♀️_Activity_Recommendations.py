import streamlit as st
import pandas as pd

st.title("Activity Recommendations 🏃")
st.write(
    "Take a look at which are the ideal days for this activity! (In the next 10 days)"
)
st.write(
    "If you have a different activity other than the ones listed, do try picking a similar activity. The activities listed cover diverse enough attribute prioritisation to fit most scenarios!"
)
st.write(
    "Note: The recommended days are ranked from most ideal at the top, at shows the top 5 best days."
)
st.write(
    """
        ***
        """
)

activity = st.selectbox(
    "Activity",
    ("Sports 🏃", "BBQ 🍖", "Drying clothes 👕", "Indoor activities 🎮", "Picnic 🧺"),
)

future_df = pd.read_csv("weather_forecast.csv", parse_dates=True, index_col=0).head(10)

if activity == "Sports 🏃":
    st.write("#### Ideal days for sports:")
    data = future_df.copy(deep=True)
    data.sort_values(
        by=["predicted_precip", "uvindex", "temp", "humidity"],
        inplace=True,
        ascending=[True, True, True, True],
    )
    for day in data.head().index:
        with st.container(border=True):
            st.write("#### " + str(day.to_pydatetime().date()))
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.write("Rainfall:")
                st.write("{:.2f}".format(data["predicted_precip"][day]))
            with col2:
                st.write("UV Index:")
                st.write("{:.2f}".format(data["uvindex"][day]))
            with col3:
                st.write("Temperature:")
                st.write("{:.2f}".format(data["temp"][day]))
            with col4:
                st.write("Humidity")
                st.write("{:.2f}".format(data["humidity"][day]))
elif activity == "BBQ 🍖":
    st.write("#### Ideal days for BBQ:")
    data = future_df.copy(deep=True)
    data.sort_values(
        by=["predicted_precip", "humidity", "temp", "windspeed"],
        inplace=True,
        ascending=[True, False, False, False],
    )
    for day in data.head().index:
        with st.container(border=True):
            st.write("#### " + str(day.to_pydatetime().date()))
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.write("Rainfall:")
                st.write("{:.2f}".format(data["predicted_precip"][day]))
            with col2:
                st.write("Humidity:")
                st.write("{:.2f}".format(data["humidity"][day]))
            with col3:
                st.write("Temperature:")
                st.write("{:.2f}".format(data["temp"][day]))
            with col4:
                st.write("Wind Speed")
                st.write("{:.2f}".format(data["windspeed"][day]))

elif activity == "Drying clothes 👕":
    st.write("#### Ideal days for drying clothes:")
    data = future_df.copy(deep=True)
    data.sort_values(
        by=["predicted_precip", "humidity", "temp", "windspeed", "uvindex"],
        inplace=True,
        ascending=[True, True, False, False, False],
    )
    for day in data.head().index:
        with st.container(border=True):
            st.write("#### " + str(day.to_pydatetime().date()))
            col1, col2, col3, col4, col5 = st.columns(5)
            with col1:
                st.write("Rainfall:")
                st.write("{:.2f}".format(data["predicted_precip"][day]))
            with col2:
                st.write("Humidity:")
                st.write("{:.2f}".format(data["humidity"][day]))
            with col3:
                st.write("Temperature:")
                st.write("{:.2f}".format(data["temp"][day]))
            with col4:
                st.write("Wind speed")
                st.write("{:.2f}".format(data["windspeed"][day]))
            with col4:
                st.write("UV Index")
                st.write("{:.2f}".format(data["uvindex"][day]))
elif activity == "Picnic 🧺":
    st.write("#### Ideal days for a picnic:")
    data = future_df.copy(deep=True)
    data.sort_values(
        by=["predicted_precip", "temp", "windspeed"],
        inplace=True,
        ascending=[True, True, False],
    )
    for day in data.head().index:
        with st.container(border=True):
            st.write("#### " + str(day.to_pydatetime().date()))
            col1, col2, col3 = st.columns(3)
            with col1:
                st.write("Rainfall:")
                st.write("{:.2f}".format(data["predicted_precip"][day]))
            with col2:
                st.write("Temperature")
                st.write("{:.2f}".format(data["humidity"][day]))
            with col3:
                st.write("Wind speed:")
                st.write("{:.2f}".format(data["windspeed"][day]))
elif activity == "Indoor activities 🎮":
    st.write("#### Ideal days for indoor activities:")
    future_df.sort_values(
        by=["predicted_precip", "uvindex"], inplace=True, ascending=[False, False]
    )
    for day in future_df.head().index:
        with st.container(border=True):
            st.write("#### " + str(day.to_pydatetime().date()))
            col1, col2 = st.columns(2)
            with col1:
                st.write("Rainfall:")
                st.write("{:.2f}".format(future_df["predicted_precip"][day]))
            with col2:
                st.write("UV index:")
                st.write("{:.2f}".format(future_df["uvindex"][day]))
