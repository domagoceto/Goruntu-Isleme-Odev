import cv2
import numpy as np

cam = cv2.VideoCapture(0)

cv2.namedWindow("frame")



while cam.isOpened():
    
    ret, frame = cam.read()
    
    
    
    if not ret:
        break
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    lower = np.array([0,100,100])
    upper = np.array([10,255,255])
    

    mask = cv2.inRange(hsv, lower, upper)
    res = cv2.bitwise_and(frame, frame, mask=mask)
    
    cv2.imshow("frame", frame)
    cv2.imshow("res", res)
        
    if cv2.waitKey(1) & 0xFF == ord("m"):
        break
    
    
cv2.destroyAllWindows()