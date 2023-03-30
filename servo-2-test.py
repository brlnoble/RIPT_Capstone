import ServoMovement

leftPins = [6,13]

leftStr = [0,0]
leftHook = [45,90]
leftUp = [90,0]

leftServo = ServoMovement.RIPT_Servo(leftPins,leftStr,leftUp,leftHook)


rightPins = [23,24]

right1 = [75,90]
right2 = [160,90]
right3 = [120,0]

rightServo = ServoMovement.RIPT_Servo(rightPins,right1,right2,right3)

while True:
	leftServo.move_servo("straight")
	rightServo.move_servo("straight")
	input()
	leftServo.move_servo("uppercut")
	rightServo.move_servo("uppercut")
	input()
	leftServo.move_servo("hook")
	rightServo.move_servo("hook")
	input()
