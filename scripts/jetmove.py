#! /usr/bin/env python3

import rospy
from jetbot_ros.msg import keycon
from jetbot import Robot

print('start!')
rospy.init_node('DCMotor')

robot=Robot()

def callback(msg):
    robot.forward(msg.Front)
    robot.left(msg.Left)
    robot.right(msg.Right)

sub = rospy.Subscriber("/Keyboard",keycon,callback)

rospy.spin()