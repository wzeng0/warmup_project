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

    def scan_callback(self, data):
        # Finds what angle at which the robot should turn
        lowest_angle = -1 # this is an initialization that tells me whether there is anything around the robot's environemnt
        smallest_val = 100 # this just has to be a big enough number so that I can figure out which angle detects an object the closest
        for x in range(360): # in range of 360 because that is the many angles that we check
            if (data.ranges[x] < smallest_val) and (data.ranges[x] != 0):
                smallest_val = data.ranges[x] # gives the distance of the angle that is closest to an object
                lowest_angle = x # the angle that is closest to the object

        if (lowest_angle == -1): # if there is nothing in the environment, then don't move
            self.twist.angular.z = 0
            self.twist.linear.x = 0
        else:
            # Rotates left and right according to where an object is found
            if (lowest_angle >= 180):
                # 1.82 is the highest speed the robot can turn
                # 180 is to keep it in the range 0 and -1 (or 0 and 1) for now
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