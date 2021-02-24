#! /usr/bin/env python3

import rospy
from std_msgs.msg import Int32
from jetbot_ros.msg import keycon
import time
import ServoSerial

rospy.init_node('Servo')
servo_device = ServoSerial.ServoSerial()
#Please type 'sudo chmod 777 /dev/ttyTHS1' on Termianl

def callback(msg):
    print(msg)
    servo_device.Servo_serial_double_control(1,msg.ServoX,2,msg.ServoY)


    
    

sub = rospy.Subscriber("/Keyboard",keycon,callback)

rospy.spin()



