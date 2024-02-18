import streamlit_authenticator as stauth
from auth import fetch_users,signup
import streamlit as st
try:
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
    email, authentication_status, username = Authenticator.login(':green[Login]', 'main')
    info, info1 = st.columns(2)
    if not authentication_status:
        signup()
    if username:
        if username in usernames:
            if authentication_status:
                    # let User see app
                st.sidebar.subheader(f'Welcome {username}')
                Authenticator.logout('Log Out', 'sidebar')

                st.markdown("""
                <style>
                    header.css-1avcm0n.ezrtsby2{
                                visibility:hidden;
                    }
                    </style>
                    """,unsafe_allow_html=True)
except:
    st.success("")