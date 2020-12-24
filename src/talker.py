#!/usr/bin/env python
import roslib; roslib.load_manifest('beginner_tutorials')  
import rospy
import time 
from std_msgs.msg import String
def talker(): 
    pub = rospy.Publisher('chatter', String) 
    rospy.init_node('talker') 
    while not rospy.is_shutdown():
        time_loc  = time.localtime()
        time_text = time.strftime("%H:%M:%S", time_loc)

        str = "\nVybornov  I.I. %s  Vagner V.A. %s  Ogordnikov A.K. %s" %(time_text, time_text, time_text)
        rospy.loginfo(str) 
        pub.publish(String(str)) 
        rospy.sleep(1.0)

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException: pass
