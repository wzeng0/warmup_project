#!/usr/bin/env python3
import rospy
# from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist, Vector3

class DriveSquare(object):
    def __init__(self):
        #initializing ros node
        rospy.init_node('Drive_in_square')
        # setting the publisher to /cmd_vel ROS topic
        self.robot_movement_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

        # Create a default twist msg (all values 0).
        lin = Vector3()
        ang = Vector3()
        self.twist = Twist(linear=lin,angular=ang)
        self.side_count = 0
    
    def square(self):
        while(self.side_count != 4):
            #code to go forward

            #how much we want the turtlebot to move forward every time
            self.twist.linear.x = 2
            # sleeps for 1 second before publishing
            rospy.sleep(1.08)
            #publishes  and goes forward for 5 seconds
            self.robot_movement_pub.publish(self.twist)
            
            # code to rotate
            # to get bot to stop moving
            self.twist.linear.x = 0

            #angle of rotation
            self.twist.angular.z = 1.57
            
            # how long to stop before publish
            rospy.sleep(2)

            # robot rotates
            self.robot_movement_pub.publish(self.twist)
            self.twist.angular.z = 0
            self.side_count += 1
        
        #stop the bot from moving 
        self.twist.linear.x = 0
        self.twist.angular.z = 0
        self.robot_movement_pub.publish(self.twist)
    
    def run(self):
        self.square()

if __name__ == '__main__':
    node = DriveSquare()
    node.run()