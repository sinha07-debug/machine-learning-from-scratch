import streamlit as st
import pandas as pd
import requests

# Load training data
df = pd.read_excel("Data_Train.xlsx")

st.title("Flight Price Predictor")

airline=st.selectbox(
    "Airline",
    sorted(df["Airline"].unique())
)
source = st.selectbox(
    "Source",
    sorted(df["Source"].unique())
)

destination = st.selectbox(
    "Destination",
    sorted(df["Destination"].unique())
)

stops = st.selectbox(
    "Total Stops",
    sorted(df["Total_Stops"].dropna().unique())
)

additional_info = st.selectbox(
    "Additional Info",
    sorted(df["Additional_Info"].unique())
)

journey_day=st.number_input(
    "journey day",
    min_value=1,
    max_value=31
)

journey_month = st.number_input(
    "Journey Month",
    min_value=1,
    max_value=12
)

# Departure Time
dep_hour = st.number_input(
    "Departure Hour",
    min_value=0,
    max_value=23
)

dep_min = st.number_input(
    "Departure Minute",
    min_value=0,
    max_value=59
)

arrival_hour = st.number_input(
    "Arrival Hour",
    min_value=0,
    max_value=23
)

arrival_min = st.number_input(
    "Arrival Minute",
    min_value=0,
    max_value=59
)

duration_hours = st.number_input(
    "Duration Hours",
    min_value=0
)

duration_mins = st.number_input(
    "Duration Minutes",
    min_value=0,
    max_value=59
)

if st.button("Predict Price"):

    payload = {
        "Airline": airline,
        "Source": source,
        "Destination": destination,
        "Total_Stops": stops,
        "Additional_Info": additional_info,
        "Journey_Day": journey_day,
        "Journey_Month": journey_month,
        "Dep_Hour": dep_hour,
        "Dep_Min": dep_min,
        "Arrival_Hour": arrival_hour,
        "Arrival_Min": arrival_min,
        "Duration_Hours": duration_hours,
        "Duration_Mins": duration_mins
    }

response=requests.post(
    "http://127.0.0.1:5000/predict",
    json=payload
)

result = response.json()

st.success(
    f"Predicted Price: ₹{result['Predicted Price']}"
)