import cv2 as cv
import mediapipe as mp
import time

def rescale_frame(img, scale = 0.2):
    width = int(img.shape[1] * scale)
    height = int(img.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(img, dimensions, interpolation=cv.INTER_AREA)

mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose
pose = mpPose.Pose()


cap = cv.VideoCapture("D:\Learn Programming\Computer Vision\OpenCV Advanced\human.mp4")
pTime = 0
while True:
    success, img = cap.read()
    
    imgRGB = cv.cvtColor(img, cv.COLOR_RGB2BGR)
    results = pose.process(imgRGB)
    print(results.pose_landmarks)
    
    if results.pose_landmarks:
        mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)
        for id, lm in enumerate(results.pose_landmarks.landmark):
            h, w, c = img.shape
            print(id, lm)
            cx, cy = int(lm.x*w), int(lm.y*h)
            cv.circle(img, (cx, cy), 10, (255, 0, 0), cv.FILLED)    
    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime
    
    cv.putText(img, str(int(fps)), (70, 70), cv.FONT_HERSHEY_COMPLEX, 3, (255, 0, 0), 3)
    
    # cv.imshow("Video", img)
    frame_resize = rescale_frame(img,scale=.2)
    cv.imshow("Video", frame_resize)
    if cv.waitKey(10) & 0xff == ord("q"):
        break
cap.release()
cv.destroyAllWindows()