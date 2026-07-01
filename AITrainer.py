import cv2
import mediapipe as mp
import time
import PoseEstimationModule as Pose
import numpy as np

cap=cv2.VideoCapture("Video1.mp4")
cap.set(3,1280)
cap.set(4,960)

PoseEstimator=Pose.PoseEstimator()
count=0
dire=0
right = True
left = False
while True:
    success,img=cap.read()
    if not success:
        break
    # img=PoseEstimator.posedetection(img)
    lmList=PoseEstimator.findPosition(img,draw=False)
    if len(lmList)!=0:
        img,angle1=PoseEstimator.findAngle(img,lmList[11][1:],lmList[13][1:],lmList[15][1:])
        img,angle2=PoseEstimator.findAngle(img,lmList[12][1:],lmList[14][1:],lmList[16][1:])
        if angle1>180:
            angle1=360-angle1
        if angle2>180:
            angle2=360-angle2
        if right:
            perRight=np.interp(angle1,(40,170),(0,100))
            barRight=np.interp(angle1,(40,170),(700,200))
            cv2.rectangle(img,(1130,200),(1170,700),(255,255,255),3)
            cv2.rectangle(img,(1130,int(barRight)),(1170,700),(0,255,0),cv2.FILLED)
            cv2.putText(img,f"{int(perRight)}%",(1120,170),cv2.FONT_HERSHEY_PLAIN,2,(255,255,255),2)
            # cv2.putText(img,f"{int(angle1)}",(40,60),cv2.FONT_HERSHEY_PLAIN,2,(0,255,0),2)
        if left:
            perLeft=np.interp(angle2,(40,170),(0,100))
            barLeft=np.interp(angle2,(40,170),(700,200))
            cv2.rectangle(img,(110,200),(150,700),(255,255,255),3)
            cv2.rectangle(img,(110,int(barLeft)),(150,700),(0,255,0),cv2.FILLED)
            cv2.putText(img,f"{int(perLeft)}%",(100,170),cv2.FONT_HERSHEY_PLAIN,2,(255,255,255),2)
            # cv2.putText(img,f"{int(angle2)}",(40,60),cv2.FONT_HERSHEY_PLAIN,2,(0,255,0),2)
        if perRight>=99:
            if dire==0:
                count+=0.5
                dire=1
        if perRight<=1:
            if dire==1:
                count+=0.5
                dire=0
        cv2.rectangle(img,(1180,600),(1280,740),(10,0,100),cv2.FILLED)
        cv2.putText(img,str(int(count)),(1210,700),cv2.FONT_HERSHEY_PLAIN,5,(255,255,255),5)
        if perLeft>=99:
            if dire==0:
                count+=0.5
                dire=1
        if perLeft<=1:
            if dire==1:
                count+=0.5
                dire=0
        cv2.rectangle(img,(0,600),(100,740),(10,0,100),cv2.FILLED)
        cv2.putText(img,str(int(count)),(30,700),cv2.FONT_HERSHEY_PLAIN,5,(255,255,255),5)
    cv2.imshow("Video",img)
    if cv2.waitKey(1)&0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()