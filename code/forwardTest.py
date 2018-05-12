import RPi.GPIO as GPIO
from time import sleep
from Line_Follower import Line_Follower 

lf = Line_Follower()
test = []
base_speed = 30
new_speed = 45
 
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
 
Motor1A = 16
Motor1B = 18
Motor1E = 22
 
Motor2A = 19
Motor2B = 21
Motor2E = 23

Motor3A = 36
Motor3B = 38
Motor3E = 40

Motor4A = 33
Motor4B = 35
Motor4E = 37
 
GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1E,GPIO.OUT)
 
GPIO.setup(Motor2A,GPIO.OUT)
GPIO.setup(Motor2B,GPIO.OUT)
GPIO.setup(Motor2E,GPIO.OUT)

GPIO.setup(Motor3A,GPIO.OUT)
GPIO.setup(Motor3B,GPIO.OUT)
GPIO.setup(Motor3E,GPIO.OUT)

GPIO.setup(Motor4A,GPIO.OUT)
GPIO.setup(Motor4B,GPIO.OUT)
GPIO.setup(Motor4E,GPIO.OUT)

p1 = GPIO.PWM(Motor1E, 200)
p2 = GPIO.PWM(Motor2E, 200)
p3 = GPIO.PWM(Motor3E, 200)
p4 = GPIO.PWM(Motor4E, 200)

p1.start(0)
p2.start(0)
p3.start(0)
p4.start(0)

intersection = True

while intersection:

	GPIO.output(Motor1A,GPIO.LOW)
	GPIO.output(Motor1B,GPIO.HIGH)
	p1.ChangeDutyCycle(base_speed)
 
	GPIO.output(Motor2A,GPIO.HIGH)
	GPIO.output(Motor2B,GPIO.LOW)
	p2.ChangeDutyCycle(base_speed)

	GPIO.output(Motor3A,GPIO.LOW)
	GPIO.output(Motor3B,GPIO.HIGH)
	p3.ChangeDutyCycle(base_speed)

	GPIO.output(Motor4A,GPIO.HIGH)
	GPIO.output(Motor4B,GPIO.LOW)
	p4.ChangeDutyCycle(base_speed)

	test = lf.read_digital()
#	print test


#increase PWM for left side to correct straight path
	
	count = 0
	
	while test[1]:

		test = lf.read_digital()
		
		p1.ChangeDutyCycle(new_speed)

		p4.ChangeDutyCycle(new_speed)

#check for intersections

		if test[0] == 1:

			count = count + 1

			print "Left"


#check for right hand turn

		if test[4] == 1:
			
			count = count +1

			print "right"

		if count > 15:

			break

#return to base_speed

	p1.ChangeDutyCycle(base_speed)

	p4.ChangeDutyCycle(base_speed)

	if count > 10:

		break

	count = 0

#increase PWM for right side to correct straight path
	
	while test[3]:

		test = lf.read_digital()

		p2.ChangeDutyCycle(new_speed)

		p3.ChangeDutyCycle(new_speed)

#check for intersections

		if test[0] == 1:

			count = count + 1

			print "Left"


#check for right hand turn

		if test[4] == 1:
			
			count = count +1

			print "right"

		if count > 15:

			break

	p2.ChangeDutyCycle(base_speed)

	p3.ChangeDutyCycle(base_speed)

	if count > 10:

		break

#check for intersections

	if test[0] == 1:

		test = lf.read_digital()

		print "Left"

		break

#check for right hand turn

#	test = lf.read_digital()

	count = 0

	if test[4] != 0:

		test = lf.read_digital()

		print "right"

		break


	count = 0

	while test[2] != 1:
		
		count = count + 1
		test = lf.read_digital()

		if count == 40:

			break
	if count == 40:
		break

p1.stop()
p2.stop()
p3.stop()
p4.stop()

sleep(1)

print test

test1 = lf.read_digital()
print test1

GPIO.cleanup()
