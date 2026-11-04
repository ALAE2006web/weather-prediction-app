import streamlit as st
import pandas as pd
import joblib

# 1. Load the trained model
model = joblib.load('weather_model.joblib')

# 2. App Title
st.set_page_config(page_title="Weather Prediction App", page_icon="🌧️")
st.title("🌧️ Rain Prediction App")
st.write("Enter the weather details below to predict if it will rain tomorrow in Australia.")

st.header("Weather Details")

# 3. Input fields
col1, col2 = st.columns(2)
with col1:
    min_temp = st.number_input("Min Temperature (°C)", value=15.0, step=1.0)
    rainfall = st.number_input("Rainfall (mm)", value=0.0, step=0.1)
    humidity9am = st.number_input("Humidity at 9am (%)", value=60.0, step=1.0)
with col2:
    max_temp = st.number_input("Max Temperature (°C)", value=25.0, step=1.0)
    humidity3pm = st.number_input("Humidity at 3pm (%)", value=50.0, step=1.0)

# 4. Prediction Button
if st.button("Predict Rain Tomorrow"):
    # Create a dataframe with the exact columns as the model expects
    input_data = pd.DataFrame(0, index=[0], columns=model.feature_names_in_)
    
    # Update the main features with user input
    input_data['MinTemp'] = min_temp
    input_data['MaxTemp'] = max_temp
    input_data['Rainfall'] = rainfall
    input_data['Humidity9am'] = humidity9am
    input_data['Humidity3pm'] = humidity3pm

    # Make prediction
    prediction = model.predict(input_data)
    
    # Show result
    st.markdown("---")
    if prediction[0] == 1:
        st.error("🌧️ *Yes, it will rain tomorrow!* (Take an umbrella ☔)")
    else:
        st.success("☀️ *No, it will not rain tomorrow.* (Enjoy the weather 🌞)")
    
