<!--Added HTML to resize image-->
<img src = "/misc/newpaltzlogo.jpg" width="40%">

# Spring 2018 Embedded Linux Class

This is my repositiory for all my documents and class work for **CPS342**. 
All work here is my own, unless otherwise noted:

1. **Personal Information:**  
  
   Name: *Seraphim Dmitrieff*  
  
   Major: *Computer Science*  
   
   ID: [N03512799](https://github.com/N03512799)  
   
   Year: *Senior*

1. **Class Start Date:** Jan 22, 2018

1. **Class End Date:** May 8, 2018

*****************************************************************************

	Design of Final Project is located in docs under Final Project Design
	
	Photos of project available in misc folder
	
	Code for Maze Solver and test code available in code folder

**Project Group Breakdown:**

	David: Assisted with design issues pertaining to power supply as well as 
	calibrating the IR Line Sensor. He did build a setup using the Line Sensor given
	but due to time constraints and lack of hardware the setup was no useable
	
		Project commitment (15%): missed too many group meetings
		
	Michael: Researched H-Bridges and useable GPIO pins had some code available to
	test motor control. Assisted with debugging vehicle and contributing to interim
	and final Reports
	
		Project Commitment (35%): Worked consistently on motors, was present to help debug most issues
		
	Seraphim: Assembled vehicle, organized cables, coded motor control, maze solving algorithm, 
	 and return code to backtrack best path taken, purchased line sensor used in final vehicle.
	 
		Project Commitment (50%): Unable to work on final vehicle until weekend before
		due to lack of other components.
		
**Can the vehicle follow a straight line?** 
	The vehicle can follow a straight line, with forward movement continuing until an intersection is detected or a dead end is reached. 

**Can the vehicle follow a bent line?**
	The vehicle uses PWM control on the enable lines on all the motors to adjust for bent paths. There are 5 sensors on our IR sensor, indexed 0-4. The middle sensor, index 2, is used to detect it the robot is currently on a path while the 2 adjacent sensors, indices 1 and 3 detect if the robot is drifting from the path and when a line is detected on either sensor, the movement coding increases the duty cycles to the opposite side and decreases them on the same side. It maintains this configuration until the sensor no longer detects a line and returns to a normal base line speed  

**Can the vehicle retrace its path at the end of a line?** 
	The movement function will determine if a dead end is reached. If this condition is detected the vehicle turns left until a line is detected on its middle IR sensor. A separate boolean condition is triggered to determine if the path is backtracked by assigning numeric values to the turn decisions 1,2,3,4 for left, straight, right and turning around respectively. If the path is being backtracked the current decision added to the decision currently at the top of the turns stack equals 4 and both values are discarded. If the sum is less than 4 the new value is appended to the turns stack and recognized as a more optimal path 

**How is target defined?** 
	The target is defined by a large rectangular area that will read all 5 IR sensors to be true once encountered.

**Can the vehicle find its target?**
	Yes, however speed of turning needs to be adjusted otherwise return algorithm will not work

**What’s the algorithm used to find the target?**
 	A left-hand rule algorithm is implemented to solve the maze. The robot is instructed to continue along a path until an intersection or a dead end is reached. The program uses the line sensor data to make a decision and executes it based on prioritizing left, then straight then right then turning around. One the function for the turn is executes the program loops and prompts the movement function once again. The program continues this loop until the maze end condition is met 

**Once target is reached, can the vehicle retrace the path next time?** 
	The vehicle uses a stack to track its movements removing any backtracked turns. Upon reaching the end of the maze the vehicle turns around and returns to the start of the Maze using the most optimal Path taken, avoid any dead ends and backtracked paths 

**Is the vehicle construction clean?**
	Yes, see misc section for photos

**Are the motor control and maze solver codes organized and commented?** 
	All coding used in the maze solver can be found in code folder
