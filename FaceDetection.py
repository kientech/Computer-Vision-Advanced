import cv2 as cv
import mediapipe as mp
import time


pTime = 0
mpFaceDetection = mp.solutions.face_detection
mpDraw = mp.solutions.drawing_utils
faceDetection = mpFaceDetection.FaceDetection()


# Rescale video define
def rescale_frame(frame, scale=0.2):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

capture = cv.VideoCapture(r"D:\Learn Programming\Computer Vision\OpenCV Advanced\person.mp4")
# capture = cv.VideoCapture(0)

while True:
    iTrue, frame = capture.read()
    imgBGR = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    result = faceDetection.process(imgBGR)
    print(result)
    
    if result.detections:
        for id, detection in enumerate(result.detections):
            mpDraw.draw_detection(frame, detection)
            
            
    # Rescale method
    frame_resize = rescale_frame(frame,scale=.2)
    
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv.putText(frame_resize, f'FPS: {int(fps)}', (70, 70), cv.FONT_HERSHEY_COMPLEX, 3, (0, 255, 0), 2)

    
    cv.imshow("Video", frame_resize)
    
    if cv.waitKey(1) & 0xFF == ord("q"):
        break
    

capture.release()
cv.destroyAllWindows()