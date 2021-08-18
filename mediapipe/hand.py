#this code is writen by fitsum tesfaye

import time
import numpy as np
import mediapipe as mp
import cv2

cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    #print(results.multi_hand_landmarks)


    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:

            for id, lm in enumerate(handLms.landmark):
                #print(id, lm)
                h, w, c =img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                # print(id, cx, cy)
                #if id == 20:
                cv2.circle(img, (cx, cy), 15, (255, 255, 255), cv2.FILLED)
                cv2.putText(img,str(id),(cx,cy),cv2.FONT_HERSHEY_SIMPLEX, 1,(255,255,255),2)



            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)



    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)) ,(10,70), cv2.FONT_HERSHEY_PLAIN, 3, (255,255,255), 3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)

