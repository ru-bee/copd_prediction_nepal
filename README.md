# Predicting Chronic Obstructive Pulmonary Disease (COPD) in Nepal
## Objective
To predict the likelihood of a patient developing Chronic Obstructive Pulmonary Disease (COPD) based on various risk factors and patient characteristics.

## Factors that Lead to COPD
- Biomass Fuel Exposure (Indoor Air Pollution)
- Tobacco Smoking
- Outdoor Air Pollution
- Occupational Exposure
- Genetic Susceptibility
- Respiratory Infections
- Low Awareness and Health Access
- Climate and Environmental Factors
## Signs and Symptoms of COPD
- Chronic Cough
- Shortness of Breath (Dyspnea)
- Excess Mucus Production (Sputum)
- Wheezing
- Fatigue and Low Energy
- Chest Tightness
- Frequent Respiratory Infections
- Cyanosis (Bluish Lips or Fingernail Beds)
- Unintended Weight Loss
- Chronic Bronchitis and Emphysema Symptoms
- Frequent Flare-ups (Exacerbations)
## Rationale for Using Synthetic Data
Due to the lack of available real-world datasets for COPD prediction in Nepal, where health data is not systematically recorded, synthetic data is used as a viable alternative. It allows for controlled simulations of patient profiles, facilitates model testing and validation, and addresses ethical concerns regarding patient privacy. This approach enables initial research efforts that can later inform real-world applications as actual data becomes available.

## Dataset
Source: Synthetic dataset created to mimic potential real-world scenarios.
Features:
- Age
- Gender
- Smoking Status
- Biomass Fuel Exposure
- Occupational Exposure
- Family History of COPD
- BMI
- Location
- Air Pollution Level
- COPD Diagnosis (target variable)
## Methodology
### Data Preprocessing
Loading the Dataset: The synthetic dataset is loaded using Pandas.
Exploring Data Types: Analyzed the data types and unique values of each feature.
Label Encoding: Categorical features were converted to numerical format using Label Encoding.
Feature Engineering: Created new features like Pollution Exposure Index and Risk Exposure Score to enhance model performance.
### Exploratory Data Analysis (EDA)
Generated histograms, box plots, scatter plots, and a correlation matrix to visualize the relationships and distributions of features.
### Model Development
Train-Test Split: The dataset was split into training (80%) and testing (20%) sets.
Model Training: Logistic Regression, Decision Trees, and Random Forest models were trained on the training set.
Hyperparameter Tuning: Used Grid Search with cross-validation to optimize model parameters.
Model Evaluation: Each model was evaluated using metrics like Accuracy, Precision, Recall, F1-Score, and AUC-ROC.
### Best Model Selection
The model with the highest accuracy was selected and saved for future use.

## Deployment
The dashboard for the COPD prediction model will be developed using Streamlit, allowing users to input patient data and receive predictions.
