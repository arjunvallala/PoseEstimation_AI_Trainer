import cv2
import mediapipe as mp
import time
import math
class PoseEstimator:
    def __init__(self,mode=False,
                 upBody = False,
                 smooth=True,detCon=0.5,trackCon=0.5):
        self.mode = mode
        self.upBody = upBody
        self.smooth= smooth
        self.detCon = detCon
        self.trackCon=trackCon

        self.mpdraw = mp.solutions.drawing_utils
        self.mppose= mp.solutions.pose
        self.pose = self.mppose.Pose()
        
    def posedetection(self,img,draw=True):
        imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(imgRGB)
        if self.results.pose_landmarks:
            if draw:
                self.mpdraw.draw_landmarks(img,                                         self.results.pose_landmarks,
                                           self.mppose.POSE_CONNECTIONS)
        return img
        
    def findPosition(self,img,draw=True):
        imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(imgRGB)
        lmList =[]
        if self.results.pose_landmarks:
            for id,lm in enumerate(self.results.pose_landmarks.landmark):
                h,w,c = img.shape
                cx,cy = int(lm.x * w),int(lm.y * h)
                lmList.append([id,cx,cy])
                if draw:
                    cv2.circle(img,(cx,cy),5,(0,250,140),cv2.FILLED)
        return lmList
        
    def findAngle(self,img,p1,p2,p3,draw=True):
        x1,y1=p1[:]
        x2,y2=p2[:]
        x3,y3=p3[:]
        
        angle = math.degrees(math.atan2(y3-y2,x3-x2)-math.atan2(y1-y2,x1-x2))
        if angle < 0:
            angle +=360
    
        if draw:
            cv2.line(img,(x1,y1),(x2,y2),(255,255,255),3)
            cv2.line(img,(x3,y3),(x2,y2),(255,255,255),3)
            cv2.circle(img,(x1,y1),10,(0,0,255),cv2.FILLED)
            cv2.circle(img,(x1,y1),15,(0,0,255),2)
            cv2.circle(img,(x2,y2),10,(0,0,255),cv2.FILLED)
            cv2.circle(img,(x2,y2),15,(0,0,255),2)
            cv2.circle(img,(x3,y3),10,(0,0,255),cv2.FILLED)
            cv2.circle(img,(x3,y3),15,(0,0,255),2)
            cv2.putText(img,str(int(angle)),(x2+30,y2+30),cv2.FONT_HERSHEY_PLAIN,3,(30,40,100),3)
        return img,angle
        
