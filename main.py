import cv2
from cvzone.HandTrackingModule import HandDetector
import socket

width,height=1280,720
#Webcam
cap=cv2.VideoCapture(0)
cap.set(3,height)
cap.set(4,width)

#Hand Detector
detector=HandDetector(maxHands=1,detectionCon=0.8)

# communication
#what is dcp look into it
sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
serverAdressPort=("localhost",8080)

while(True):
    #Get frame from webcam
    success, img = cap.read()

    #Find the hand
    hands,img=detector.findHands(img)

    data=[]
    # Landmark values (x,y,z)*21
    if hands:
        hand=hands[0]
        lmList=hand['lmList']
        for lm in lmList:
            #reverse y direction for unity
            data.extend([lm[0], height - lm[1], lm[2]])
        sock.sendto(str.encode(str(data)), serverAdressPort)



    cv2.imshow("Image",img)
    cv2.waitKey(1)


