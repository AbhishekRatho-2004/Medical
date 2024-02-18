import streamlit as st
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler as scalar
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split



parkinsons_data = pd.read_csv('parkinsons.csv')

X = parkinsons_data[['MDVP:Fo(Hz)','MDVP:Fhi(Hz)','MDVP:Flo(Hz)','MDVP:Jitter(%)','MDVP:Jitter(Abs)','MDVP:RAP','MDVP:PPQ']]
Y = parkinsons_data['status']

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=2)






model = svm.SVC(kernel='linear')
model.fit(X_train, Y_train)

def predict_parkinsons(input_data):
    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
    prediction = model.predict(input_data_reshaped)
    return prediction


def brainDisease():
    parkinsons_data = pd.read_csv('parkinsons.csv')

    X = parkinsons_data[['MDVP:Fo(Hz)','MDVP:Fhi(Hz)','MDVP:Flo(Hz)','MDVP:Jitter(%)','MDVP:Jitter(Abs)','MDVP:RAP','MDVP:PPQ']]
    Y = parkinsons_data['status']

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=2)






    model = svm.SVC(kernel='linear')
    model.fit(X_train, Y_train)
    st.title('Parkinson\'s Disease Prediction')
    st.write('This app predicts whether a person has Parkinson\'s disease based on input features.')

    st.header('Input Features')
    input_features = {
        'MDVP:Fo(Hz)': st.number_input('MDVP:Fo(Hz)', min_value=0.0, max_value=300.0, value=0.0),
        'MDVP:Fhi(Hz)': st.number_input('MDVP:Fhi(Hz)', min_value=0.0, max_value=300.0, value=0.0),
        'MDVP:Flo(Hz)': st.number_input('MDVP:Flo(Hz)', min_value=0.0, max_value=300.0, value=0.0),
        'MDVP:Jitter(%)': st.number_input('MDVP:Jitter(%)', min_value=0.0, max_value=1.0, value=0.0),
        'MDVP:Jitter(Abs)': st.number_input('MDVP:Jitter(Abs)', min_value=0.0, max_value=1.0, value=0.0),
        'MDVP:RAP': st.number_input('MDVP:RAP', min_value=0.0, max_value=1.0, value=0.0),
        'MDVP:PPQ': st.number_input('MDVP:PPQ', min_value=0.0, max_value=1.0, value=0.0),
    }


    if st.button('Predict'):
        input_data = [input_features[feature] for feature in X]
        prediction = predict_parkinsons(input_data)
        st.write(prediction)
        if all(pred == 0 for pred in prediction):
            st.error('The person does not have Parkinson\'s disease.')
        else:
            st.success('The person has Parkinson\'s disease.')
