import streamlit as st
import mysql.connector
from streamlit_option_menu import option_menu
import streamlit.components.v1 as components
from Footer import footer
import cv2
import mediapipe as mp 
from AIFit import repcounter
from brain import brainDisease
from Predict import prediction
from chatbot import bot
from News import news
from recommendation import recommend

# Function to authenticate users
def authenticate(username, password):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="password",
            database="healthapp"
        )
        cursor = conn.cursor()
        query = "SELECT * FROM users WHERE uname = %s AND password = %s"
        cursor.execute(query, (username, password))
        user = cursor.fetchone()
        conn.close()
        if user:
            return True
    except Exception as e:
        st.error(f"Error: {e}")
    return False

# Function to create a new user
def create_user(username, password):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="password",
            database="healthapp"
        )
        cursor = conn.cursor()
        query = "INSERT INTO users (uname, password) VALUES (%s, %s)"
        cursor.execute(query, (username, password))
        conn.commit()
        conn.close()
        return True
    except mysql.connector.IntegrityError:
        return False
    except Exception as e:
        st.error(f"Error: {e}")
        return False

# Authenticate the user
def login():
    st.sidebar.subheader("Login")
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")
    if st.sidebar.button("Login"):
        if authenticate(username, password):
            return True
        else:
            st.sidebar.error("Incorrect username or password")
    return False

# Register a new user
def register():
    st.sidebar.subheader("Register")
    new_username = st.sidebar.text_input("New Username")
    new_password = st.sidebar.text_input("New Password", type="password")
    confirm_password = st.sidebar.text_input("Confirm Password", type="password")
    if new_password == confirm_password:
        if st.sidebar.button("Register"):
            if create_user(new_username, new_password):
                st.sidebar.success("Registration successful. Please login.")
            else:
                st.sidebar.error("Username already exists.")
    else:
        st.sidebar.error("Passwords do not match")

if not login():
    register()
    st.stop()

# Rest of your Streamlit app code...


menu = option_menu(
    menu_title=None,
    options=["🏠Home", "📈Predict", "📊Recommend", "💪AIfit", "📰News", "🤖Bot"],
    orientation="horizontal",
    menu_icon="cast",
    icons=[':home:' for i in range(8)],
    styles={
        'container': {"background-color": "white ", "border": '2px solid black', 'width': '1360px',
                      'height': '65px'},
        'nav-link': {'font-size': '18.3px', 'font-weight': 'bold', 'text-align': 'center', 'color': 'black',
                     'margin-top': '-3.5px', 'margin-left': '-3.4px', '--hover-color': 'violet', 'height': '51px'},
        'nav-link-selected': {"background-color": 'skyblue', 'color': 'white'}
    }
)

try:
    if menu == "🏠Home":
        st.write("Home")
        footer()
    if menu == "📈Predict":
        prediction()
        footer()
    if menu == "📊Recommend":
        st.write("Recommend")
        recommend()
        footer()
    if menu == "💪AIfit":
        repcounter()
        footer()
    if menu == "📰News":
        st.write("News")
        news()
        footer()
    if menu == "🤖Bot":
        bot()
except Exception as e:
    st.success("Sorry")
