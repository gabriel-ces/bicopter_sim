#!/usr/bin/env python

import rospy
import math

from std_msgs.msg import Float64, Float64MultiArray, MultiArrayDimension, MultiArrayLayout
from math import sin,cos,atan2,sqrt,fabs,pi

#Define a RRBot joint positions publisher for joint controllers.
def tilt_joint_positions_publisher():

	#Initiate node for controlling joint1 and joint2 positions.
	rospy.init_node('tilt_positions_node', anonymous=True)

	#Define publishers for each joint position controller commands.
	pub = rospy.Publisher('bicopter_tilt_controller/command', Float64MultiArray, queue_size=10)
	rate = rospy.Rate(100) #100 Hz
	#Defining msg as float64MultiArray
	msg = Float64MultiArray()
	msg.layout.data_offset = 0
	myMultiArrayDimensions = MultiArrayDimension()
	myMultiArrayDimensions.label = ''
	myMultiArrayDimensions.size = 2
	myMultiArrayDimensions.stride = 1
	msg.layout.dim.append(myMultiArrayDimensions)

	#While loop to have joints follow a certain position, while rospy is not shutdown.
	i = 0
	while not rospy.is_shutdown():
		
		#Have each joint follow a sine movement of sin(i/100).
		#msg.data = [0.00,0.00]
		
		#Have each joint follow a sine movement of sin(i/100).
		msg.data = [(math.pi/2)*abs(sin(i/500.)),(math.pi/2)*abs(sin(i/500.))]

		#Publish the same sine movement to each joint.
		pub.publish(msg)
		i = i+1 #increment i

		rate.sleep() #sleep for rest of rospy.Rate(100)

#Main section of code that will continuously run unless rospy receives interuption (ie CTRL+C)
if __name__ == '__main__':
	try: tilt_joint_positions_publisher()
	except rospy.ROSInterruptException: pass