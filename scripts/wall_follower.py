#!/usr/bin/env python3

import rospy
# imports scan to get information about environment
from sensor_msgs.msg import LaserScan
# from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist, Vector3

# how close the robot will stay from the person it is following
distance = 0.8

class FollowPerson(object):
    def __init__(self):
        # initialize ros node
        rospy.init_node('follow_person')
        # setting publisher to /cmd/vel
        self.movement_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        # subscribing to /scan
        self.scan_pub = rospy.Subscriber('/scan', LaserScan, self.scan_callback)

        # Create a default twist msg (all values 0).
        lin = Vector3()
        ang = Vector3()
        self.twist = Twist(linear=lin,angular=ang)
        # self.scan_pub = LaserScan(range_max = .8)

    def scan_callback(self, data):
        # Finds what angle at which the robot should turn
        lowest_angle = -1
        smallest_val = 100
        # Looks through data set to see which
        for x in range(360):
            if (data.ranges[x] < smallest_val) and (data.ranges[x] != 0):
                smallest_val = data.ranges[x]
                lowest_angle = x

        if (lowest_angle == -1):
            self.twist.angular.z = 0
            self.twist.linear.x = 0
        else:
            # this is for adjusting the robot so that it is a set distance away from the wall
            # This accounts for when the robot is too close to the wall
            if (data.ranges[lowest_angle] < distance):
                # If the robot is facing inward, I want it to face away from the wall
                if (lowest_angle <= 90):
                    self.twist.angular.z = ((lowest_angle + 90) / 180) * 1.82
                elif (lowest_angle >= 270):
                    self.twist.angular.z = (-(360 - lowest_angle - 90) / 180) * 1.82
                else: # This is if the robot is already facing outwards
                    self.twist.angular.z = 0
            # This accounts for when the robot is too far from the wall
            elif (data.ranges[lowest_angle] > distance):
                # If it is 90 degrees, my formula will make the turn 0 which is not what
                # I want so I gave 90 a separate condition
                if (lowest_angle == 90):
                    self.twist.angular.z = ((lowest_angle - 45) / 45) * 1.82
                # This is if the bot is facing outwards and it is too far from the wall 
                # then I want it to face the wall
                elif (lowest_angle > 90) and (lowest_angle <= 180):
                    self.twist.angular.z = ((lowest_angle - 90) / 90) * 1.82
                elif (lowest_angle <= 270) and (lowest_angle > 180):
                    self.twist.angular.z = (-(360 - lowest_angle + 90) / 180) * 1.82
                else: # If it is already facing inwards then do nothing
                    self.twist.angular.z = 0
            # Rotates left and right according to where an object is found
            elif (lowest_angle >= 90) and (lowest_angle < 270):
                # This twist adjusts the robot to 90 degress
                self.twist.angular.z = (-(360 - lowest_angle - 270) / 180) * 1.82
            else:
                if (lowest_angle < 90):
                    self.twist.angular.z = ((lowest_angle - 90) / 90) * 1.82
                else:
                    self.twist.angular.z = (-(360 - lowest_angle - 270) / 90) * 1.82
            #overall forward force of the robot
            self.twist.linear.x = 0.1

        # publishes the movement accordingly
        self.movement_pub.publish(self.twist)
    # runs the function
    def run(self):
        rospy.spin()
if __name__ == '__main__':
    node = FollowPerson()
    node.run() 

