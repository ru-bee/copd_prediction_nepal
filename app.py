import streamlit as st
import pandas as pd
import pickle

# Load the best model
model_name = "Logistic_Regression.pkl"  
with open(model_name, 'rb') as model_file:
    model = pickle.load(model_file)

st.title("COPD Prediction Dashboard")

# Sidebar for user input
st.sidebar.header("User Input Features")

def user_input_features():
    age = st.sidebar.slider("Age", min_value=0, max_value=100, value=50)
    gender = st.sidebar.selectbox("Gender", ["Male", "Female"])
    smoking_status = st.sidebar.selectbox("Smoking Status", ["Non-smoker", "Former smoker", "Current smoker"])
    
    # Change these features to Yes/No inputs
    biomass_fuel_exposure = st.sidebar.selectbox("Biomass Fuel Exposure", ["Yes", "No"])
    occupational_exposure = st.sidebar.selectbox("Occupational Exposure", ["Yes", "No"])
    family_history_copd = st.sidebar.selectbox("Family History of COPD", ["Yes", "No"])
    
    # Replace BMI slider with selectable categories
    bmi_category = st.sidebar.selectbox("BMI Category", ["Underweight", "Normal", "Overweight", "Obese"])
    location = st.sidebar.selectbox("Location", ["Urban", "Rural"])
    
    # Change Respiratory Infections in Childhood to Yes/No
    respiratory_infections = st.sidebar.selectbox("Respiratory Infections in Childhood", ["Yes", "No"])
    
    data = {
        'Age': age,
        'Gender': gender,
        'Smoking_Status': smoking_status,
        'Biomass_Fuel_Exposure': biomass_fuel_exposure,
        'Occupational_Exposure': occupational_exposure,
        'Family_History_COPD': family_history_copd,
        'BMI': bmi_category,
        'Location': location,
        'Air_Pollution_Level': 'Yes' if st.sidebar.checkbox("Air Pollution Level (Yes)", value=True) else 'No',
        'Respiratory_Infections_Childhood': respiratory_infections,
    }
    features = pd.DataFrame(data, index=[0])
    return features

input_features = user_input_features()

# Prediction
if st.button("Predict COPD Diagnosis"):
    # Preprocess input features similar to your training data
    input_features['Gender'] = input_features['Gender'].map({'Male': 1, 'Female': 0})
    input_features['Smoking_Status'] = input_features['Smoking_Status'].map({"Non-smoker": 0, "Former smoker": 1, "Current smoker": 2})
    input_features['Family_History_COPD'] = input_features['Family_History_COPD'].map({"Yes": 1, "No": 0})
    input_features['Location'] = input_features['Location'].map({"Urban": 1, "Rural": 0})

    # Map BMI categories to numeric values
    bmi_mapping = {
        "Underweight": 0,
        "Normal": 1,
        "Overweight": 2,
        "Obese": 3
    }
    input_features['BMI'] = input_features['BMI'].map(bmi_mapping)

    # Map Yes/No features to binary values
    input_features['Biomass_Fuel_Exposure'] = input_features['Biomass_Fuel_Exposure'].map({"Yes": 1, "No": 0})
    input_features['Occupational_Exposure'] = input_features['Occupational_Exposure'].map({"Yes": 1, "No": 0})
    input_features['Air_Pollution_Level'] = input_features['Air_Pollution_Level'].map({"Yes": 1, "No": 0})
    input_features['Respiratory_Infections_Childhood'] = input_features['Respiratory_Infections_Childhood'].map({"Yes": 1, "No": 0})

    # Create additional features
    input_features['Pollution_Exposure_Index'] = input_features['Air_Pollution_Level'] * input_features['Biomass_Fuel_Exposure']
    input_features['Risk_Exposure_Score'] = input_features['Smoking_Status'] + input_features['Occupational_Exposure'] + input_features['Biomass_Fuel_Exposure']

    # Define the order of features as the model was trained
    feature_order = [
        'Age', 
        'Gender', 
        'Smoking_Status', 
        'Biomass_Fuel_Exposure', 
        'Occupational_Exposure', 
        'Family_History_COPD', 
        'BMI', 
        'Location', 
        'Air_Pollution_Level', 
        'Respiratory_Infections_Childhood', 
        'Pollution_Exposure_Index',  
        'Risk_Exposure_Score'
    ]

    # Reorder the DataFrame to match model training
    input_features = input_features[feature_order]

    # Prediction
    prediction = model.predict(input_features)
    st.write("COPD Diagnosis Prediction:", "Yes" if prediction[0] == 1 else "No")

