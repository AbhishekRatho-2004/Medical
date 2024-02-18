import streamlit as st
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score



def disease():
    diabetes_dataset = pd.read_csv('diabetes.csv')
# Prepare data for training
    X = diabetes_dataset.drop(columns='Outcome', axis=1)
    Y = diabetes_dataset['Outcome']

    # Standardize the data
    scaler = StandardScaler()
    scaler.fit(X)
    X_scaled = scaler.transform(X)

    # Split the data into training and testing sets
    X_train, X_test, Y_train, Y_test = train_test_split(X_scaled, Y, test_size=0.2, stratify=Y, random_state=2)

    # Train the SVM classifier
    classifier = svm.SVC(kernel='linear')
    classifier.fit(X_train, Y_train)

    # Function to predict diabetes
    def predict_diabetes(input_data):
        input_data_as_numpy_array = np.asarray(input_data)
        input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
        std_data = scaler.transform(input_data_reshaped)
        prediction = classifier.predict(std_data)
        return prediction
    st.title('Diabetes Prediction')
    st.write('This app predicts whether a person has diabetes based on input features.')

    # Input features
    st.header('Input Features')
    input_features = {
        'Pregnancies': st.number_input('Pregnancies',key=34, min_value=0, max_value=20, value=0),
        'Glucose': st.number_input('Glucose', min_value=0,key=35, max_value=200, value=0),
        'BloodPressure': st.number_input('BloodPressure',key=36, min_value=0, max_value=150, value=0),
        'SkinThickness': st.number_input('SkinThickness',key=37, min_value=0, max_value=100, value=0),
        'Insulin': st.number_input('Insulin', min_value=0,key=38,max_value=1000, value=0),
        'BMI': st.number_input('BMI', min_value=0.0, key=39,max_value=50.0, value=0.0),
        'DiabetesPedigreeFunction': st.number_input('DiabetesPedigreeFunction',key=40,min_value=0.0, max_value=2.0, value=0.0),
        'Age': st.number_input('Age',key=41, min_value=0, max_value=120, value=0)
    }

    # Predict button
    if st.button('Predict',key=6):
        input_data = [input_features[feature] for feature in X.columns]
        prediction = predict_diabetes(input_data)
        if prediction[0] == 0:
            st.error('The person is not diabetic.')
        else:
            st.success('The person is diabetic.')

disease()
