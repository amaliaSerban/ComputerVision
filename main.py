import cv2
from cvzone.HandTrackingModule import HandDetector

#Webcam
cap=cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)

#Hand Detector
detector=HandDetector(maxHands=1,detectionCon=0.8)


while(True):
    #Get frame from webcam
    success, img = cap.read()
    #Find the hand
    hands=detector.findHands(img)
    cv2.imshow("Image",img)
    cv2.waitKey(1)


