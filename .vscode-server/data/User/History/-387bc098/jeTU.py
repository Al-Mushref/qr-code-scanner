#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import PoseStamped


def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.pose)

def listener():
    rospy.init_node('qr_code_listener', anonymous=True)
    rospy.Subscriber("/visp_auto_tracker/object_position", PoseStamped, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()