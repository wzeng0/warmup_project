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
