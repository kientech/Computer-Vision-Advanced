import cv2 as cv
import mediapipe as mp
import time


cap = cv.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw  = mp.solutions.drawing_utils

cTime = 0
pTime = 0

while True:
    success, img = cap.read()
    imgRGB =  cv.cvtColor(img, cv.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    # print(results.multi_hand_landmarks)
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                # print(id, lm)
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                print(id, cx, cy)
                if id == 0:
                    cv.circle(img, (cx, cy), 10, (255, 0, 255), cv.FILLED)

                if id == 1:
                    cv.circle(img, (cx, cy), 10, (163, 198, 150), cv.FILLED)
                    
                if id == 2:
                    cv.circle(img, (cx, cy), 10, (13, 15, 22), cv.FILLED)
                    
                if id == 3:
                    cv.circle(img, (cx, cy), 10, (112, 117, 126), cv.FILLED)
                    
                if id == 4:
                    cv.circle(img, (cx, cy), 10, (166, 165, 151), cv.FILLED)

                if id == 5:
                    cv.circle(img, (cx, cy), 10, (105, 90, 151), cv.FILLED)
                    
                if id == 6:
                    cv.circle(img, (cx, cy), 10, (147, 145, 46), cv.FILLED)
                    
                if id == 7:
                    cv.circle(img, (cx, cy), 10, (73, 56, 46), cv.FILLED)

                if id == 8:
                    cv.circle(img, (cx, cy), 10, (253, 114, 158), cv.FILLED)

                if id == 9:
                    cv.circle(img, (cx, cy), 10, (117, 42, 57), cv.FILLED)
                    
                if id == 10:
                    cv.circle(img, (cx, cy), 10, (32, 42, 167), cv.FILLED)
                    
                if id == 11:
                    cv.circle(img, (cx, cy), 10, (15, 17, 126), cv.FILLED)

                if id == 12:
                    cv.circle(img, (cx, cy), 10, (300, 0, 300), cv.FILLED)

                if id == 13:
                    cv.circle(img, (cx, cy), 10, (163, 19, 10), cv.FILLED)
                    
                if id == 14:
                    cv.circle(img, (cx, cy), 10, (130, 15, 22), cv.FILLED)
                    
                if id == 15:
                    cv.circle(img, (cx, cy), 10, (112, 180, 126), cv.FILLED)
                    
                if id == 16:
                    cv.circle(img, (cx, cy), 10, (25, 0, 25), cv.FILLED)

                if id == 17:
                    cv.circle(img, (cx, cy), 10, (63, 198, 10), cv.FILLED)
                    
                if id == 18:
                    cv.circle(img, (cx, cy), 10, (13, 90, 32), cv.FILLED)
                    
                if id == 19:
                    cv.circle(img, (cx, cy), 10, (12, 300, 26), cv.FILLED)
                    
                if id == 20:
                    cv.circle(img, (cx, cy), 10, (25, 250, 55), cv.FILLED)

                if id == 21:
                    cv.circle(img, (cx, cy), 10, (63, 198, 50), cv.FILLED)

                    
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
    
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    
    cv.putText(img, str(int(fps)), (10, 70), cv.FONT_HERSHEY_COMPLEX, 3, (255, 0, 255), 3)
    
    if cv.waitKey(30) & 0xff == ord('q'):
        break
    
    
    cv.imshow("Webcam", img)
cap.release()
cv.destroyAllWindows()