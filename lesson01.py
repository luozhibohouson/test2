'''
Author: luozhibohouson 178215804@qq.com
Date: 2024-10-13 18:49:02
LastEditors: luozhibohouson 178215804@qq.com
LastEditTime: 2024-10-19 17:55:01
FilePath: \opencv-python\lesson01.py
Description: 

Copyright (c) 2024 by luozhibo, All Rights Reserved. 
'''

import numpy as np
import cv2 as cv
def face_detect_methed():
    # 图片灰度化
    grey_img = cv.cvtColor(img_resized,cv.COLOR_BGRA2GRAY)
    # 定义分类器，使用OpenCV自带的分类器
    face_detector = cv.CascadeClassifier('C:/Users/Administrator/AppData/Roaming/Python/Python313/site-packages/cv2/data/haarcascade_frontalface_alt.xml')
    # 使用分类器
    face = face_detector.detectMultiScale(grey_img,1.1,5,0,(10,10),(200,200))
    # 在图片中对人脸画矩阵
    for x,y,w,h in face:
        cv.rectangle(img_resized,(x,y),(x+w,y+h),color=(0,0,255),thickness=2)
    cv.imshow('result',img_resized)

img = cv.imread("faceMorePeople.jpg")  #读取当前路径下的图像文件lena,jpg
#修改尺寸
img_resized = cv.resize(img,(500,500))
face_detect_methed()
#按下m键时退出程序
while True:
    if ord('m') == cv.waitKey(0):
        break
cv.destroyAllWindows()       #用户一旦输入任意键后，程序关闭窗口