#!/usr/bin/env python
import roslib; roslib.load_manifest('beginner_tutorials')
import rospy 
from std_msgs.msg import String

def callback(data):
    rospy.loginfo('\nI heard: %s', data.data)

if __name__ == '__main__':
    rospy.init_node('listener', anonymous = True)
    rospy.Subscriber('chatter', String, callback)

    rospy.spin()
