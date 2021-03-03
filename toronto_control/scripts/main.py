#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import Float64

def talker():
    pub = rospy.Publisher('/simple_model/base_to_second_joint_position_controller/command', Float64, queue_size=10)
    rospy.init_node('robot_talker', anonymous=False)
    rate = rospy.Rate(0.5) # 0.5hz
    while not rospy.is_shutdown():
        #hello_str = "hello world %s" % rospy.get_time()
	#newPose = LinkState()
	#newPose.link name=""
	#newPose.pose=10.0
	position= 100.0
        rospy.loginfo(position) #printa il numero nella shell
        pub.publish(position) #pubblica nel topic
        rate.sleep()

if __name__ == '__main__':
    try:
	#print "Launching talker() node..."
        talker()
    except rospy.ROSInterruptException:
        pass
