#! /usr/bin/env python3

import cv2
import rospy
from cv_bridge import CvBridge
from sensor_msgs.msg import Image

rospy.init_node("Camera_Pub")
pub=rospy.Publisher("/Video",Image,queue_size=1)
# rate=rospy.Rate(10)

#OPENCV SCIRPTS
cap = cv2.VideoCapture("nvarguscamerasrc ! video/x-raw(memory:NVMM), width=(int)1280, height=(int)720, format=(string)NV12, framerate=(fraction)60/1 ! nvvidconv flip-method=0 ! video/x-raw, width=(int)1280, height=(int)720, format=(string)BGRx ! videoconvert ! video/x-raw, format=(string)BGR ! appsink", cv2.CAP_GSTREAMER)

print(cap.isOpened())

while not rospy.is_shutdown() :
    ret,img=cap.read()
    img_RGB = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    msg_frame = CvBridge().cv2_to_imgmsg(img_RGB)
    pub.publish(msg_frame)
    # rate.sleep()



cap.release()
cv2.destroyAllWindows()