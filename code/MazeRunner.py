

#Define initial variables:

#turns acts as a stack to track the movements made by our robot
#decision interprets the data from the IR sensor allowing the next turn decision to be made

turns = []
decision = []
turnAround = False
notAtEnd = True

while notAtEnd:

#Move Robot forward until an intersection is detected return IR sensor readings to decision  
  
  decision = move()

#Check if Robot has reached end of maze if not execute next turn decision
	
  if all(decision):
    notAtEnd = False
	  
#Left turn has priority, then straight, then right turn lastly if not turns detected robot will turn around 
   
  else:
    if decision[:1] == 1:
	  turns.append(1)
	  turnLeft()
	elif decision[2:6] == 1:
	  turns.append(2)
	elif decision[5:] == 1:
	  turns.append(3)
	  turnRight()
	else:
	  turns.append(4)
	  turnAround()
	  turnAround = True

#If Robot turns around previous turns will be removed while backtracking maze
		
  if turnAround:
	check = turns.pop()
	  
#turn around value will be discarded from list, if value is not 4 turn decision is checked for backtracking	

	if check != 4:
	  check = check + turns.pop()
		
#If check value equals 4 means that turn is being backtracked by robot and will be discarded from list

	  if check != 4:
		turns.append(check)
		turnAround = False

#Once end of maze is reached, robot will turn around and return to start of maze using best path taken 		  

turnAround()
    
while len(turns)>0:
  
  move()
	
  nextMove = turns.pop()
	
  if nextMove == 1:
	turnRight()
  elif nextMove == 2:
#move forward
  else:
	turnLeft()
	  
#Define Movement functions

def turnLeft():
#code to have motors turn robot 90 degrees to left


def turnRight():
#code to have motors turn robot 90 degrees to right

def turnAround():
#code to have motors turn robot 180 degrees

def move():
  
	