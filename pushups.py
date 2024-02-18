import cv2
import numpy as np
import cvzone
from cvzone.PoseModule import PoseDetector
import math
import streamlit as st

counter = 0
direction = 0

# Initialize PoseDetector and capture device
pd = PoseDetector(trackCon=0.70, detectionCon=0.70)
cap = cv2.VideoCapture(0)  # Use camera index 0 for the default camera

st.title("AI Push Up Counter")

# Function to calculate angles and count push-ups
def angles(lmlist, p1, p2, p3, p4, p5, p6, drawpoints):
    global counter
    global direction

    if len(lmlist) != 0:
        point1 = lmlist[p1]
        point2 = lmlist[p2]
        point3 = lmlist[p3]
        point4 = lmlist[p4]
        point5 = lmlist[p5]
        point6 = lmlist[p6]

        x1, y1 = point1[1]  # Changed to index 1 for x-coordinate
        x2, y2 = point2[1]
        x3, y3 = point3[1]
        x4, y4 = point4[1]
        x5, y5 = point5[1]
        x6, y6 = point6[1]

        if drawpoints == True:
            cv2.circle(img, (x1, y1), 10, (255, 0, 255), 5)
            # Draw other points and lines here

        lefthandangle = math.degrees(math.atan2(y3 - y2, x3 - x2) -
                                      math.atan2(y1 - y2, x1 - x2))

        righthandangle = math.degrees(math.atan2(y6 - y5, x6 - x5) -
                                       math.atan2(y4 - y5, x4 - x5))

        # Calculate angles and count push-ups here

# Streamlit app
while True:
    ret, img = cap.read()

    if not ret:
        st.write("Error reading camera feed.")
        break

    # Resize image if necessary
    img = cv2.resize(img, (500, 500))

    # Perform pose detection and push-up counting
    lmlist, bbox = pd.findPosition(img, draw=0, bboxWithHands=0)
    angles(lmlist, 11, 13, 15, 12, 14, 16, drawpoints=1)

    # Convert image to RGB for Streamlit
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Display image in Streamlit
    st.image(img_rgb, channels="RGB")

    if st.button("Exit"):
        break
