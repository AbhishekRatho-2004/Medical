import streamlit as st
import streamlit_authenticator as stauth
from dependancies import sign_up, fetch_users
import streamlit as st
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
from home import Home
from Excercise import excercise
st.set_page_config(
                page_title="M E D F R N D",
                page_icon="🧊",
                layout="wide",
                initial_sidebar_state="expanded",
                )
users = fetch_users()
emails = []
usernames = []
passwords = []


for user in users:
    emails.append(user['key'])
    usernames.append(user['username'])
    passwords.append(user['password'])

credentials = {'usernames': {}}
for index in range(len(emails)):
    credentials['usernames'][usernames[index]] = {'name': emails[index], 'password': passwords[index]}

Authenticator = stauth.Authenticate(credentials, cookie_name='Streamlit', key='abcdef', cookie_expiry_days=4)
#fields: dict, default {'Form name':'Login', 'Username':'Username', 'Password':'Password', 'Login':'Login'}
email, authentication_status, username = Authenticator.login(fields={'Form name':'Login', 'Username':'Username', 'Password':'Password', 'Login':'Login'})
#':green[Login]', 'main'
info, info1 = st.columns(2)

if not authentication_status:
    sign_up()
if username:
    if username in usernames:
        if authentication_status:
                # let User see app
            st.sidebar.subheader(f'Welcome {username}')
            Authenticator.logout('Log Out', 'sidebar')
            
            menu=option_menu(
                menu_title=None,
                options=["🏠Home","📈Predict","📊Recommend","💪AIfit","📰News","🤖Bot"],
                orientation="horizontal",
                menu_icon="cast",
                icons=[':home:' for i in range(8)],
                styles={
                            'container':{"background-color":"white ","border":'2px solid black','width':'1360px','height':'65px'},
                            'nav-link':{'font-size':'18.3px','font-weight':'bold','text-align':'center','color':'black','margin-top':'-3.5px','margin-left':'-3.4px','--hover-color':'violet','height':'51px'},
                            'nav-link-selected':{"background-color":'skyblue','color':'white'}
                        }
                )
            if menu=="🏠Home":
                Home()
                footer()
            if menu=="📈Predict":
                prediction()
                footer()
            if menu=="📊Recommend":
                st.write("Recommend")
                recommend()
                footer()
            if menu=="💪AIfit":
                excercise()
                footer()
            if menu=="📰News":
                news()
                footer()
            if menu=="🤖Bot":
                bot()
        elif not authentication_status:
            with info:
                st.error('Incorrect Password or username')
        else:
            with info:
                st.warning('Please feed in your credentials')
    else:
        with info:
            st.warning('Username does not exist, Please Sign up')



