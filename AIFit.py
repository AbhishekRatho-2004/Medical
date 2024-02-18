import streamlit as st
import cv2
import cv2
import mediapipe as mp

def repcounter():
    mpDraw = mp.solutions.drawing_utils
    mpPose = mp.solutions.pose
    pose = mpPose.Pose()
    up = False
    counter = 0
    count=0
    st.title("REP COUNTER")
    st.caption("Fit yourself using AI")
    cap = cv2.VideoCapture(0)
    frame_placeholder = st.empty()
    stop_button_pressed = st.button("Stop")
    while cap.isOpened() and not stop_button_pressed:
        ret, img = cap.read()
        if not ret:
            st.write("Video Capture Ended")
            break
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = pose.process(imgRGB)
        
        if results.pose_landmarks:
            mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)
            points = {}
            for id, lm in enumerate(results.pose_landmarks.landmark):
                h,w,c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
            
                points[id] = (cx,cy)


            cv2.circle(img, points[12], 15, (255,0,0), cv2.FILLED)
            cv2.circle(img, points[14], 15, (255,0,0), cv2.FILLED)
            cv2.circle(img, points[11], 15, (255,0,0), cv2.FILLED)
            cv2.circle(img, points[13], 15, (255,0,0), cv2.FILLED)


            if not up and points[14][1] + 40 < points[12][1]:
                
                up = True
                counter += 1
            elif points[14][1] > points[12][1]:
                
                up = False
        

        cv2.putText(img, str(counter), (100,150),cv2.FONT_HERSHEY_PLAIN, 12, (255,0,0),12)

        frame = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        frame_placeholder.image(frame,channels="RGB")
        if cv2.waitKey(1) & 0xFF == ord("q") or stop_button_pressed:
            count=counter
            break
        if stop_button_pressed:
            st.write(f"Number of reps:{counter}")
    st.write(f"Number of reps:{count}")
    cap.release()   
    cv2.destroyAllWindows()
    
