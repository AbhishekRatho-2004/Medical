import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn import svm
import numpy as np
from sklearn.model_selection import train_test_split


def main():
    df = pd.read_csv('SaYoPillow.csv')


    x = df[['snoring range', 'respiration rate', 'blood oxygen levels', 'heart rate']]
    y = df['sl']

    scaler = StandardScaler()
    scaler.fit(x)
    standardized_data = scaler.transform(x)
    x = standardized_data

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

 
    classifier = svm.SVC(kernel='linear')

  
    classifier.fit(x_train, y_train)


    def predict_parkinsons(input_data):

        input_data_as_numpy_array = np.asarray(input_data)
        input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
       
        std_data = scaler.transform(input_data_reshaped)
       
        prediction = classifier.predict(std_data)
        return prediction

    st.title('Stress detection')
    st.write('This app predicts stress level based on input features.')

    st.header('Input Features')
    snoring_range = st.number_input('Snoring Range', min_value=0, max_value=100, value=0)
    respiration_rate = st.number_input('Respiration Rate', min_value=0, max_value=100, value=0)
    blood_oxygen_levels = st.number_input('Blood Oxygen Levels', min_value=0, max_value=100, value=0)
    heart_rate = st.number_input('Heart Rate', min_value=0, max_value=100, value=0)

    if st.button('Predict',key=1):
        input_data = (snoring_range, respiration_rate, blood_oxygen_levels, heart_rate)
        prediction = predict_parkinsons(input_data)
        if prediction[0] == 0:
            st.success('Your stress level is 0 gently do activites like walking stretching  or deep breathing exercises')
        elif(prediction[0] == 1):
            st.success('Your stress level is 1 perform aerobic exercises such as jogging, cycling')
        elif(prediction[0]==2):
            st.error('Your stress level is 2 moderatly perform activites like swimming, yoga')
        elif(prediction[0]==3):
            st.error('Your stress level is 3 so do intense workouts like weight lifting , running')
        else:
            st.warning('Your stress level is 4 so please consider more calming activities like meditation, mindfullness if and also consult docter')
