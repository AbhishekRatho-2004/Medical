import streamlit as st
def footer():
    st.markdown('---')
    f1,f2,f3=st.columns(3)
    with f1:
        st.subheader(':red[Company]')
        st.text('About Us')
        st.markdown("Services")
        st.markdown("Predictions")
        
        st.markdown("Compare")
    with f2:
        st.subheader(':red[Get Help]')
        scrn = 'https://community-aw7lbr3iqk2geknhj9spxa.streamlit.app/'
        st.markdown("[Community](%s)" % scrn)
        scrn = 'https://gymbros.streamlit.app/'
        st.markdown("[BMI](%s)" % scrn)
        st.text('Health')
        st.text('News')
    with f3:
        st.subheader(':red[Connect Us]')
        st.text('Email')
        st.text('FaceBook')
        st.text('LinkedIn')
        st.text('Twitter')