
# -*- coding: utf-8 -*-
"""
Created on Thu May 20 10:01:41 2021

@author: GWJIANG
"""

import cv2
import time
import os
import HandTrackingModule as htm

wCam, hCam = 320, 240

cap = cv2.VideoCapture(r"C:\Users\GWJIANG\Videos\iVCam\2021-07-09 003546.mp4")

cap.set(3, wCam)
cap.set(4, hCam)

folderPath = r"C:\Users\GWJIANG\Desktop\GW\python code\HandProject\FingerImages"
myList = os.listdir(folderPath)
print(myList)
overlayList = []
for imPath in myList:
    image = cv2.imread(f'{folderPath}/{imPath}')
    # print(f'{folderPath}/{imPath}')
    overlayList.append(image)

print(len(overlayList))
pTime = 0

#detector = htm.handDetector(detectionCon=0.75)

tipIds = [4, 8, 12, 16, 20]
i=0
while True:
    success, img = cap.read()
  #  img = detector.findHands(img)
   
    #lmList = detector.findPosition(img, draw=False)
    # print(lmList)


#        h, w, c = overlayList[totalFingers - 1].shape
#        img[0:h, 0:w] = overlayList[totalFingers - 1]



    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime


    cv2.imshow("Image", img)
    if i%5==0:
        cv2.imwrite(r'C:\Users\GWJIANG\Desktop\GW\python code\yolov4\downloads\test\8_data'+str(i)+'.jpg', img)
    i = i+1
    cv2.waitKey(10)