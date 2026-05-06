import streamlit as st
import pickle
import pandas as pd

# Load model
with open("models/model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("🏠 House Price Prediction App")

st.write("Enter details below:")

# Inputs
area = st.number_input("Enter Area (sq ft)", min_value=500, max_value=5000, step=100)
bedrooms = st.number_input("Enter Number of Bedrooms", min_value=1, max_value=10)

# Predict button
if st.button("Predict Price"):
    input_data = pd.DataFrame([[area, bedrooms]], columns=["area", "bedrooms"])
    prediction = model.predict(input_data)
    
    st.success(f"Predicted Price: ₹ {prediction[0]:.2f} Lakhs")