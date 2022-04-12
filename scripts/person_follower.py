#!/usr/bin/env python3

import rospy
# imports scan to get information about environment
from sensor_msgs.msg import LaserScan
# from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist, Vector3

# how close the robot will stay from the person it is following
distance = 0.4

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
        for x in range(360):
            if (data.ranges[x] < smallest_val) and (data.ranges[x] != 0):
                smallest_val = data.ranges[x]
                lowest_angle = x
        if (lowest_angle == -1):
            self.twist.angular.z = 0
            self.twist.linear.x = 0
        else:
            # Rotates left and right according to where an object is found
            if (lowest_angle >= 180):
                self.twist.angular.z = (-(360 - lowest_angle) / 180) * 1.82
            else:
                self.twist.angular.z = (lowest_angle / 180) * 1.82

            # stop bot if it is the distance away from object
            if (data.ranges[0] < distance) and (data.ranges[0] != 0):
                self.twist.linear.x = 0
            else:
                self.twist.linear.x = 0.1

        # publishes the movement accordingly
        self.movement_pub.publish(self.twist)

    def run(self):
        rospy.spin()
if __name__ == '__main__':
    node = FollowPerson()
    node.run() 