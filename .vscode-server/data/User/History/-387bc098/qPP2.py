#!/usr/bin/env python

import rospy
from geometry_msgs.msg import PoseStamped

def listener():
    rospy.init_node('qr_code_listener', anonymous=True)
    rospy.Subscriber("/visp_auto_tracker/object_position", PoseStamped, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()