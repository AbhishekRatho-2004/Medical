import streamlit as st
from brain import brainDisease
from Stress import main
from heart import heartdisease
from sugar import disease

def prediction():
    st.write("Predict")
    t1,t2,t3,t4=st.tabs(["Stress","Brain","Heart","Sugar"])
    with t2:
        brainDisease()
    with t1:
        main()
    with t3:
        heartdisease()
    with t4:
        disease()
