'''
Author: luozhibohouson 178215804@qq.com
Date: 2024-10-13 18:49:02
LastEditors: luozhibohouson 178215804@qq.com
LastEditTime: 2024-10-20 19:30:27
FilePath: \opencv-python\lesson01.py
Description: 

Copyright (c) 2024 by luozhibo, All Rights Reserved. 
'''

import numpy as np
import cv2 as cv
 
# 检测方法定义
def face_detect_method(img):
    grey_img = cv.cvtColor(img,cv.COLOR_BGRA2GRAY)
    face_detector = cv.CascadeClassifier("G:/conda/envs/testOpencv/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml")
    face = face_detector.detectMultiScale(grey_img,1.02,4)
    for x,y,w,h in face:
        cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    cv.imshow("result",img)
 
#读取摄像头
#cap = cv.VideoCapture(0)
#读取视频
cap = cv.VideoCapture('D:/opencv/opencv-python/tongtong.mp4')
 
# 循环判断
while True:
    flag,frame = cap.read()
    if not flag:
        break
    face_detect_method(frame)
    if ord('c')==cv.waitKey(1):
        break
 
cv.destroyAllWindows()
cap.release()