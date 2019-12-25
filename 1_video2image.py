# coding=utf-8
import cv2
import numpy as np

vc = cv2.VideoCapture("/home/duanyajun/图片/文件处理中心/9.mp4") #读入视频文件
c=1
k = 1
if vc.isOpened(): #判断是否正常打开
    rval , frame = vc.read()
else:
    rval = False
 
timeF = 1 #视频帧计数间隔频率
 
while rval:   #循环读取视频帧
    rval, frame = vc.read()
    if(c%timeF == 0): #每隔timeF帧进行存储操作
        n = 6 - len(str(k)) 
        cv2.imwrite('/home/duanyajun/图片/文件处理中心/2/' +str(0)*n + np.str(k) + '.jpg',frame) #存储名字为六位数的为图像
        k = k + 1
    c = c + 1
    cv2.waitKey(1)
vc.release()
