#! /usr/bin/env python

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
        self.side_count = 0

    def scan_callback(self, data):
        if (data.ranges[0] == 0.0 or data.ranges[0] >= distance):
            self.twist.linear.x = 0.1
        else:
            self.twist.linear.x = 0
        self.movement_pub.publish(self.twist)

    def run(self):
        rospy.spin()
if __name__ == '__main__':
    node = FollowPerson()
    node.run()