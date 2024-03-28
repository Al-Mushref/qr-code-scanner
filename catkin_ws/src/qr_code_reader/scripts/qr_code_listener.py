#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import PoseStamped

# 
def callback(data):
    """ 
     This callback function is invoked when a new PoseStamped message is received on the 
    '/visp_auto_tracker/object_position' topic. It logs the received pose information 
    to the ROS console.

    @param data: The PoseStamped message containing the pose information. This message
                 contains both the position and orientation of an object as detected
                 by the 'visp_auto_tracker'.
    """
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.pose)

def listener():
    """
    This function initializes the ROS node, creates a subscriber for the 
    '/visp_auto_tracker/object_position' topic, and enters a loop waiting for
    messages to process. This node subscribes to the topic and uses the 
    callback function to log the received pose information.

    It utilizes rospy.spin() to keep the node active and listening for new messages
    until the node is shutdown. The 'anonymous=True' parameter ensures that the node 
    has a unique name, avoiding name conflicts with other nodes.
    """
    rospy.init_node('qr_code_listener', anonymous=True)
    rospy.Subscriber("/visp_auto_tracker/object_position", PoseStamped, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()

