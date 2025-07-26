"""
Created on Sat Apr 26 13:44:57 2025

@author: NoorenMariyam
"""





import streamlit as st
import joblib

# Load the model
model = joblib.load("linear_model.pkl")

# Title and description
st.title("🍽️ Restaurant Rating Predictor")
st.markdown("Estimate your restaurant's rating based on cost, votes, and service features.")

# Input fields
cost = st.number_input("Approximate Cost for Two People (₹)", min_value=0, value=500)
votes = st.number_input("Number of Customer Votes", min_value=0, value=50)
online_order = st.radio("Online Ordering Available?", ["Yes", "No"])
book_table = st.radio("Table Booking Available?", ["Yes", "No"])

# Prepare input data
input_data = [[cost, votes, 1 if online_order == "Yes" else 0, 1 if book_table == "Yes" else 0]]

# Predict only when the button is clicked
if st.button("Predict"):
    prediction = model.predict(input_data)
    st.success(f"🎯 Predicted Rating: **{round(prediction[0], 2)} / 5** 🌟")
