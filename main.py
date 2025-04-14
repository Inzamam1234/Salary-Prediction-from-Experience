import streamlit as st
import pickle
import numpy as np

# Load model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# Title
st.title("🧑‍💼 Salary Predictor")
st.markdown("Predict your salary based on your years of experience.")

# Input
experience = st.slider("Years of Experience", 0.0, 20.0, step=0.1)

# Prediction
if st.button("Predict Salary"):
    input_data = np.array([[experience]])
    salary = model.predict(input_data)[0]
    st.success(f"💰 Estimated Salary: ₹{salary:,.2f}")
