# 🌧️ Weather Prediction in Kuala Lumpur, Malaysia

A **Streamlit-powered data product** that analyses historical weather data and forecasts rainfall patterns for Kuala Lumpur. The app features interactive data exploration, a 10-day weather forecast, activity recommendations, and a weather simulation tool, which are all driven by a machine learning prediction model.
> Built as a university group project for **WIE2003 Introduction to Data Science** at Universiti Malaya.

🔗 **Live Demo:** [wie2003-weather-app.streamlit.app](https://wie2003-weather-app.streamlit.app/)

---

## ✨ Features

| Page | Description |
|---|---|
| **🏠 Home** | Project background, objectives, and overview of the weather prediction initiative. |
| **🤔 How's the Weather** | Interactive dashboard showing monthly weather metrics (temperature, rainfall, humidity, UV index) with selectable chart views across 2016–2023. |
| **🔭 Weather Data Viewer** | Browse and filter the cleaned dataset by date range and variables, with CSV download support. |
| **🌥️ Weather Forecast** | 10-day precipitation forecast displayed as weather cards with condition icons (Clear Sky, Light/Moderate/Heavy Rain). |
| **🏃‍♀️ Activity Recommendations** | Suggests the top 5 ideal days for activities (Sports, BBQ, Drying Clothes, Picnic, Indoor Activities) based on forecasted conditions. |
| **🛰️ Weather Simulation** | Input custom weather parameters and predict rainfall intensity using the trained Ridge Regression model. |
| **📋 About** | Team information and contributors. |

---

## 📊 Data Source

Historical daily weather data for **Kuala Lumpur (2016–2023)** sourced from [Visual Crossing](https://www.visualcrossing.com/).

**Weather Stations:**
- **WMSA** — Sultan Abdul Aziz Shah International Airport
- **WMKK** — Kuala Lumpur International Airport

Key variables include temperature, feels-like temperature, dew point, humidity, precipitation, wind speed/gust/direction, sea-level pressure, cloud cover, visibility, UV index, and more.

---

## 🤖 Model Pipeline

### Model Selection

Five regression models were evaluated to predict precipitation intensity:

| Model | Type |
|---|---|
| XGBoost Regressor | Ensemble (Boosting) |
| Random Forest Regressor | Ensemble (Bagging) |
| Elastic Net | Regularised Linear |
| Ridge Regression | Regularised Linear |
| Lasso Regression | Regularised Linear |

**Ridge Regression** was selected as the best-performing model after comparison.

### Features & Engineering

The model uses **22 predictor variables** including:
- Meteorological features: temperature, humidity, dew point, wind speed/gust/direction, sea-level pressure, cloud cover, visibility, UV index, precipitation cover
- Lag features: 7-day precipitation lags (`precip_lag_1` to `precip_lag_7`)
- Rolling statistics: 7-day rolling mean and standard deviation of precipitation

A **log transformation** (`log1p`) is applied to precipitation values, and features are standardised using a **StandardScaler** before prediction.

### Forecasting

Future predictor variable values are generated using **ARIMA** (AutoRegressive Integrated Moving Average), which are then fed into the Ridge Regression model to produce 10-day precipitation forecasts.

---

## 🛠️ Tech Stack

- **Frontend & Deployment:** [Streamlit](https://streamlit.io/)
- **Data Processing:** Pandas, NumPy
- **Machine Learning:** scikit-learn, Joblib
- **Image Handling:** Pillow (PIL)

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+

### Installation

```bash
# Clone the repository
git clone https://github.com/Wrynaft/WeatherPrediction.git
cd WeatherPrediction

# Create a virtual environment (optional but recommended)
python -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Run Locally

```bash
streamlit run 🏠_Home.py
```

The app will open in your browser at `http://localhost:8501`.

---

## 📁 Project Structure

```
WeatherPrediction/
├── 🏠_Home.py                      # Main entry point & home page
├── pages/
│   ├── 1_🤔_Hows_the_weather.py    # Monthly weather dashboard
│   ├── 2_🔭_Weather_Data_Viewer.py # Data explorer with filters
│   ├── 3_🌥️_Weather_Forecast.py   # 10-day forecast display
│   ├── 4_🏃‍♀️_Activity_Recommendations.py  # Activity day ranker
│   ├── 5_🛰️_Weather_Simulation.py # Custom weather predictor
│   └── 6_📋_About.py               # Team info
├── Photos/                          # Weather condition images
├── actual_cleaned_dataset.csv       # Cleaned historical weather data
├── weather_forecast.csv             # Pre-generated 10-day forecast
├── best_rid_reg.pkl                 # Trained Ridge Regression model
├── scaler.save                      # Fitted StandardScaler
└── requirements.txt                 # Python dependencies
```

---

## 👥 Contributors

- **Ryan Chin Jian Hwa** — Project Leader & Developer
- **John Ong Ming Hom** — Data Scientist & Developer
- **Koay Khoon Lyn** — ML Model Development
- **Heng Xin Phei** — ML Model Development
- **Lavine See Yu Tian** — Data Scientist
