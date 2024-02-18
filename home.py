import streamlit as st

# Set page title and icon


# Add a header
def Home():
    
    # Add an image
    image = "team.jpg"  # Replace with the path or URL of your image
    st.image(image, caption="Healthcare Image", use_column_width=True, output_format="auto")
    st.markdown(
        """
        <h3 style="background-color: #3498db; color: #ffffff; padding: 10px; border-radius: 10px;"><marquee>Welcome to Met Frnd App</marquee></h3>
        """,
        unsafe_allow_html=True
    )
    # Add some introductory text
    st.write("Explore various healthcare features and services below.")
    st.header("Introduction")
    col1,col2=st.columns(2)
    col1.write('''Our project predominantly focuses on health and fitness,
    featuring two key sections: a fitness component and a
    prediction and prevention component. In the fitness section,
    we offer an AI trainer that guides users in performing exercises
    with precision, ensuring correct form and technique.
    Meanwhile, in the prediction and prevention section, users can
    input symptoms, allowing the system to accurately recommend
    appropriate medications. Our primary emphasis lies in
    addressing various health concerns, including heart health,
    diabetes, BMI management, stress management, and
    Parkinsons disease, facilitating early detection and informed
    decision-making for users regarding their health status.''')
    col2.image('intro.jpg', width=400)
    col1,col2=st.columns(2)
    col1.image('fit.jpg', width=200)
    col2.header('Fitness')
    col2.write('''In our fitness facility, we have incorporated an ai trainer alongside a robotic assistant to guide individuals through their exercise routines. This innovative system allows users to observe and replicate proper exercise techniques demonstrated by the robot, thereby facilitating effective workouts. ''')
    col1,col2=st.columns(2)
    col1.header('Prediction')
    col1.write('''Utilizing a comprehensive array of
    inputs including symptoms such as
    cough, cold, itching, and so on,
    our predictive system employs
    sophisticated algorithms to
    recommend the most suitable
    medication With precision and
    efficiency, our system empowers
    users to make informed choices in
    managing their health and wellbeing.''')
    col2.image('predic.jpg', width=400)
    col1,col2=st.columns(2)
    col1.image('prec.jpg', width=250)
    col2.header('Preventions')
    col2.write('''Leveraging an intricate analysis of
    symptoms, our system excels in
    forecasting diseases, providing
    detailed descriptions, and
    recommending tailored precautions,
    medications, workouts, and dietary
    regimens. Through meticulous
    examination of symptomatology,
    our platform delivers precise and
    comprehensive insights to aid in
    diagnosis and management. This
    integrated approach ensures
    holistic and personalized guidance
    for individuals seeking optimal
    health outcomes.
    ''')