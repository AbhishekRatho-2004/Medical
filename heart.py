import streamlit as st
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
def heartdisease():
# Load the heart disease dataset
    heart_data = pd.read_csv('heart_disease_data.csv')

    # Split the data into features (X) and target variable (Y)
    X = heart_data[['age','sex','cp','trestbps','chol','fbs','restecg','thalach']]
    Y = heart_data['target']

    # Split the data into training and testing sets
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=2)

    # Train a RandomForestClassifier to get feature importances
    #clf = RandomForestClassifier(random_state=42)
    #clf.fit(X_train, Y_train)

    # Select features based on a threshold
    #feature_importances = clf.feature_importances_
    #threshold = 0.07
    #selected_features = X.columns[feature_importances > threshold]

    # Select features for training and testing sets
    #X_train_selected = X_train[selected_features]
    #X_test_selected = X_test[selected_features]
    model = LogisticRegression()
    model.fit(X_train, Y_train)
    #X_train = model.predict(X_train)
    #X_test = model.predict(X_test)

    # Streamlit UI
    st.title("Heart Disease Prediction")

    # Add input fields for user to enter data
    age = st.number_input("Enter Age:", min_value=0, step=1)
    sex = st.selectbox("Select Sex", options=["Male", "Female"])
    cp = st.selectbox("Select Chest Pain Type", options=[0, 1, 2, 3])
    trestbps = st.number_input("Enter Resting Blood Pressure:", min_value=0, step=1)
    chol = st.number_input("Enter Serum Cholesterol:", min_value=0, step=1)
    fbs = st.selectbox("Fasting Blood Sugar", options=["<= 120 mg/dl", "> 120 mg/dl"])
    restecg = st.selectbox("Resting Electrocardiographic Results", options=[0, 1, 2])
    thalach = st.number_input("Enter Maximum Heart Rate Achieved:", min_value=0, step=1)

    # Button to predict
    predict_button = st.button("Predict",key=33)

    if predict_button:
        # Check if any input fields are empty
        if not all([age, sex, cp, trestbps, chol, fbs, restecg, thalach]):
            st.warning("Please enter valid values for all input fields.")
        else:
            # Convert input data to a numpy array
            sex_value = 1 if sex == "Male" else 0
            fbs_value = 1 if fbs == "> 120 mg/dl" else 0
            input_data = np.asarray([age, sex_value, cp, trestbps, chol, fbs_value, restecg, thalach])
            input_data_reshaped = input_data.reshape(1, -1)
            
            # Make prediction
            prediction = model.predict(input_data_reshaped)

            # Display the result
            if prediction[0] == 0:
                st.write('The Person does not have a Heart Disease')
            else:
                st.write('The Person has Heart Disease')
heartdisease()