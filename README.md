# warmup_project

## Drive in a Square
### Problem
The problem was to make the robot drive in a square so that it returns to its original destination.
At first, I used the spin in a circle and stop at wall functions for reference. I realize that to make the robot drive in a square, I need to incorporate both of these components. When moving in a square, the robot has to travel the length of the sides of the square and rotate 90 degrees to form the angle of the square. 

### My Approach
My approach to the problem was to separate the two movements of the roboot, namely the rotate 90 degrees and moving along the sides of a square. Therefore, I wanted to let the robot move forward first and then rotate 90, repeating this process 4 times for all 4 sides of the square.

### My Functions
In the init function, I initialized the node, publisher, as well as the twist of the robot so that the twist was 0 and the robot was not moving.
Then in the square function is where I put all the robot movement in. 
Going with the approach I had, I wanted to move the robot forward first. That brings me to the linear portion of twist where it allows me to change the x axis position of the robot. I used the rospy.sleep function before every publish statement in order for the robot to get all the variables set in place and finish running its previous command. Then in order to stop the roboot completely, I set the x variable back to 0.
After this, I had to find a way to rotate the robot 90 degrees. I knew that the twist also has a angular property where I can change the z coordinates to rotate the robot. I tested out various combinations of numbers until I got to where the robot will rotate 90 degrees. 
My next challenge was to do this process 4 times. I had to go back to the init function to set a variable to self that kept track of how many times the while loop was running. At the end of every move and turn, I incremented this count and by the time it hit 4, the roboto shouldn't be running anymore.
However, I hit my next block here where the robot kept spinning in place because the z coordinate of twist was never cleared. Therefore, at the end of the function, outside the while loop, I reinitialize the twist function to be 0 in all coordinates which concludes my move function.
My last function run, ensures that I run the square function to get the robot moving and main function executes it.

## Challenges
A challenge I faced writing this part of the project was definitely my inexperience in object-oriented python. I was mostly going along with the previous sample codes trying to figure out what each of them meant and how the process of sending signals to robots worked. I am very grateful for the TAs that helped me outside of their office hour times which was very useful. In addition to TA help, I was able to overcome my obstacles through reading into online documentation about certain rospy functions such as twist. Moreover, I found it slightly difficult to keep track of the variables such as twist and I had to remind myself to change the variables back to 0 if I don't want the robot to move like it previously did.

## Improvements
If I had time, I would try to figure out what was wrong with my rotation. I tried to test run my robot for this function many times but each time finding myself face to face to what seems like a different rotation at each vertex of the square. I think it might be largly due to the friction of the force or maybe the battery of the robots were not enough.

## GIF
![drive-in-square_1-2-2-2-2](https://user-images.githubusercontent.com/75603464/161701468-5b635369-9bad-4132-9e8f-10ea3b2005b4.gif)

## Person Follower
### Problem
The problem was to make the robot follow a person around and stops when it is a certain distance from the person it is following.
At first, I used the stop at wall function for reference since I realize that the bot will go towards the wall and stop at a certain distance. Therefore, If I can make it go forward according to a moving object, the code would be similar. I needed to use the sensor to my advantage and move the robot according to what its sensors detect.

### My Approach
My approach to this problem was to scan for the nearest object to the robot and 
change directions so that the robot faces that closest object and moves towards
it. I want the robot to only stop when it is too close to the object and if it
is not too close, keep moving forward and turning so that it faces the closest
object.

### My Functions
In the init function, I initialized the node, publisher, subscriber, as well as the twist of the robot so that the twist was 0 and the robot was not moving.
Then in the scan_callback function is where I put all the robot movement in. 
Going with the approach I had, I wanted the robot to first scan its surroundings to find the object that is closest to it assuming there is. If there isn't the robot shouldn't move at all since there is nothintg to follow. That brings me to the rotation aspect. So if there is an object that was picked up by the sensor, take the angle with the closest object and rotate so that it is facing the object at 0 degrees. I had to account for turning left or right since if the object is to the right of the robot, I didn't want the robot to turn an angle that is more than 180 from the left all the way to the right. Then I set the linear aspect of the turn to be a set forward speed since I want the roboto to be continuously moving.
My challenge with this aspect was to find a formula where I can turn angles greater than 180 to its positive counter parts. For example, if an object was detected at 270 degrees, I wanted the equation to output -90 so that the robot rotates 90 degrees to the right. I also wanted the robot turn speed to stay between 1 and -1 since a large number might not be processed. Therefore, I realized that if i divided my equation by 180, I can receive a number between 0 and -1 or 0 and 1. Then, I multiplied by 1.8 since that is the maximum turn speed of the robot and I didn't want the turning to be too slow.

## Challenges
A challenge I faced writing this part of the project was account for the error in the turn of the robot. I also had a very shallow understanding of the sensor details of the robot. For example, I did not understand that sensor.ranges was an array of size 359 and the distance an object is to the designated angle. Furthermore, I was not aware that the angle of the bot was counterclockwise which caused a lot of confusion. I was able to overcome these challenges through the diagrams and instructions of my TAs. In addition, I  used a lot of unecessary if statements which casued my code to be relatively unreadable which was also corrected through instructions from TA to help me realize which if statements were unecessary.

## Improvements
I would change the angle of rotation of my robot to turn quicker. Right now, although it is at max rotation speed, I realize that other people's robots turn relatively quicker than mine. Therefore, I would like to find out where in my code I can fix to change the rotation speed.

## GIF

## Wall Follower
### Problem
The problem was to make the robot follow a wall at a 90 degree angle nonstop at a set distance away from the wall.
At first, I realize that this function is somewhat similar to the person following function since now we just want the robot to follow the closest object to it at a 90 degree angle (or 270). Therefore, If I can make the robot keep the object to its 90 degree standard, it would be following the wall.

### My Approach
My approach to this problem was to scan for the nearest object to the robot and change its direction so that the closest object should be at at 90 degrees of the robot. I figured that if after adjustment and the robot isn't the set distance away from the wall, it would adjust itself first accordingly and then continue to follow the wall.

### My Functions
In the init function, my approach was the same as the perseon follower. I initialized the node, publisher, subscriber, as well as the twist of the robot so that the twist was 0 and the robot was not moving.
Then in the scan_callback function is where I put all the robot movement in. 
Going with the approach I had, I wanted the robot to first scan its surroundings to find the object that is closest to it assuming there is. If there isn't the robot shouldn't move at all since there is nothintg to follow.
That brings me to the rotation aspect. So if there is an object that was picked up by the sensor, take the angle with the closest object and rotate so that the robot's sensor at 90 degrees picks the object up (the wall) as the closest object. 
My particular challenge with this portion is to find a way to keep the wall at the robot's 90 degree. In the previous follow person function, I used 0 degrees, the head of the robot, to follow the person. Therefore, my approach to this was to set the "head" of  the robot to its side which was 90 degrees and pretend that is the 0 degree of the person follower. I solved this by just -90 to all the angle output of the robot and adjusted the left and right turn accordingly.

## Challenges
A challenge I faced writing this part of the project was to keep the robot a set distance away from the wall. My approach to this is to first rotate the robot so that the wall is 90 degrees from it. Then check if the distance between the wall and the 90 degree sensor is the set distance. If it is lower, then rotate out 45 degrees so that the 45 degree from 90 is far enough from the wall. Then rotate it back to 90 and follow the wall like that.

## Improvements
I think that I can improve the adapbility of the robot by setting a range of angles for the sensor since the sensor might not be too accurate. That way the bot has more leeway when moving and detecting objects.

## GIF

