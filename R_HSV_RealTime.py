import cv2
import numpy as np

cap = cv2.VideoCapture(0)

def NoFunction():
    pass

cv2.namedWindow("Ranga")

cv2.createTrackbar("Lower Hue","Ranga",0,180,NoFunction)
cv2.createTrackbar("Lower Saturation","Ranga",0,255,NoFunction)
cv2.createTrackbar("Lower Value","Ranga",0,255,NoFunction)
cv2.createTrackbar("Higher Hue","Ranga",180,180,NoFunction)
cv2.createTrackbar("Higher Saturation","Ranga",255,255,NoFunction)
cv2.createTrackbar("Higher Value","Ranga",255,255,NoFunction)

while True:
    
    ret, frame = cap.read()
    
    lh = cv2.getTrackbarPos("Lower Hue","Ranga")
    ls = cv2.getTrackbarPos("Lower Saturation","Ranga")
    lv = cv2.getTrackbarPos("Lower Value","Ranga")
    hh = cv2.getTrackbarPos("Higher Hue","Ranga")
    hs = cv2.getTrackbarPos("Higher Saturation","Ranga")
    hv = cv2.getTrackbarPos("Higher Value","Ranga")
    
    lowerRange = np.array([lh,ls,lv])
    higherRange = np.array([hh,hs,hv])
    
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    mask = cv2.inRange(hsv,lowerRange,higherRange)
    
    mask_rgb = cv2.cvtColor(mask,cv2.COLOR_GRAY2BGR)
    
    ranga = cv2.bitwise_and(frame,frame,mask = mask)
    
    stack = np.hstack((frame,mask_rgb,ranga))
    
    cv2.imshow('Ranga',cv2.resize(stack,None,fx=0.5,fy=0.5))    
    
    if cv2.waitKey(1) == ord('q'):
        break
  
# cap.release()
# cv2.destroyAllWindows()