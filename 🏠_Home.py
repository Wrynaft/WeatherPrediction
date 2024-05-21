import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Weather prediction in Kuala Lumpur, Malaysia",
    page_icon="🌧️",
    # layout="wide"  # Set the layout to wide mode
)

# Create a container for the logo and title
logo_title_container = st.container()

# Create a two-column layout for the logo and title
col1, col2 = logo_title_container.columns([1, 3])

# Add the logo image in the first column
with col1:
    image = Image.open("Raindar.jpeg")
    st.image(image, width=190)

# Add the title in the second column
with col2:
    st.markdown("""
        <div style="display: flex; align-items: center; justify-content: center; height: 100%; text-align: center; font-size: 42px; font-weight: bold; color: #FFFFFF;">
            Weather Prediction<br>in Kuala Lumpur, Malaysia 🌧️
        </div>
    """, unsafe_allow_html=True)
    
# Reset the layout to a single column for the remaining content
st.container()

st.sidebar.success("Select a page above.")

st.markdown(
    """
    ***
    ### Project Background

    Before we start doing the project, we have done several research on the case studies, and one of them has inspired us to conduct weather forecasting related topics. Case study: Weather and climate forecasting for community resilience to climate related risks and shocks was a study conducted in Uganda, the study shows the importance of weather forecasting in the local community where many of them appreciate the translation of seasonal weather forecasts into local language. Mainly, the weather forecast has helped them in their agriculture sector and created a big impact to the locals. Therefore, we plan to create a similar impact in our country. 

    Malaysia's weather is typified by its tropical climate, which has high temperatures and humidities, heavy rainfall, and a climatic year patterned around the northeast and southwest monsoons. According to the Climate Change Knowledge Portal, Malaysia experienced a mean annual precipitation of 3085.5 millimetres (mm) which is considered vastly outpacing the average annual precipitation over the world. 

    According to EPA Climate Change Indicators: Heavy Precipitation, the potential impacts of heavy precipitation include crop damage, soil erosion and an increase in flood risk due to heavy rains. However, it is reported that most Malaysians have overlooked the importance of weather forecasting in general. There are several factors that possibly lead to this scenario, they are prediction inaccuracy, limited understanding towards the prediction system and complex forecasting reports. 

    Thus, in order to increase the awareness of the public towards the local weather condition and improve resilience and preparedness across every sector to adapt to Malaysia’s precipitation level, our team has come up with a project to construct a weather prediction model. We have selected Kuala Lumpur as the target location of the prediction model. The target audience can be anyone in the city regardless of their age, sex, profession and status. Specific professions such as urban planners, transportation agencies and tourism sectors can utilise the model for economy and business driving purposes. Others might be using the model to plan their daily activities as well. The model will work around several variables such as wind speed, temperature, uv index, humidity and others to compute the precipitation levels. This model can help the local individuals to make well-informed decisions and reduce the risks associated with unfavourable weather conditions. 

    ***
    
    ### Project Objectives

    1. Raise public awareness and understanding of weather forecasting
    2. Encourage decision-making and weather-related event preparedness
    3. Analyse historical weather data and forecast rainfall patterns

"""
) 
