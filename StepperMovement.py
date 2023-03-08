import RPi.GPIO as GPIO #for IO control
from time import sleep, perf_counter #for delay functionality
import PySimpleGUI as sg #for simple interface
import random #for random positions

#Define clockwise and counter clockwise for readability
cw = GPIO.HIGH
ccw = GPIO.LOW

class Stepper:
    def __init__(self,motorPins,zeroPins):

        #Pins for the motor drivers
        self.dirPin1 = motorPins[0]
        self.dirPin2 = motorPins[1]
        self.stepPin1 = motorPins[2]
        self.stepPin2 = motorPins[3]

        #Pins for the zero positioning
        self.zeroPinX = zeroPins[0]
        self.zeroPinY = zeroPins[1]

        #Parameters of the motors
        self.speed_max_default =  150e3 #delay between pulses (200k Hz default)
        self.speed_min_default = 75e3
        self.m_delay = 0.5 #delay between movements
        self.m_steps = 1600 #steps per rotation (1/8 microstep)
        self.m_diameter = 1.215 #diameter of the motor gear in cm

        #Location tracking
        self.location = [0,0]

        #Setup the GPIO pins
        GPIO.setmode(GPIO.BCM)

        GPIO.setup(self.dirPin1,GPIO.OUT)
        GPIO.setup(self.stepPin1,GPIO.OUT)
        GPIO.setup(self.dirPin2,GPIO.OUT)
        GPIO.setup(self.stepPin2,GPIO.OUT)

        GPIO.setup(self.zeroPinX,GPIO.IN)
        GPIO.setup(self.zeroPinY,GPIO.OUT)

        #~~~~~ Return the parameters ~~~~~
        def __str__(self):
            return f"Motor Pins: {self.dirPin1},{self.dirPin2},{self.stepPin1},{self.stepPin2} \nZero Pins: {self.zeroPinX},{self.zeroPinY}"

        #~~~~~ Set the pins being used ~~~~~
        def Set_Pins(self,pins):
            self.dirPin1,self.dirPin2,self.stepPin1,self.stepPin2 = pins

        #~~~~~ Convert cm to steps ~~~~~
        def Dist_to_Steps(self,distance):
            return int( (distance / (3.14156 * self.m_diameter)) * self.m_steps) #return the number of steps as an integer

        #~~~~~ Convert steps to cm ~~~~~
        def Steps_to_Dist(self,steps):
            return (steps / self.m_steps) * (3.14156 * self.m_diameter)
            
        #~~~~~ Move motors a given number of steps ~~~~~
        def Move_Motors(self,steps,speed_max,speed_min):    
            #Accelerate over one rotation if steps and max/min speeds set
            if steps > 1600 and speed_max != speed_min:
                
                accel_step = (speed_max - speed_min)/1600 #Frequency increase per step
                
                for accel in range(0,1600):
                    
                    accel_speed = 1 / (accel_step*accel + speed_min) #New speed
                    
                    GPIO.output(self.stepPin1,GPIO.HIGH)
                    GPIO.output(self.stepPin2,GPIO.HIGH)
                    sleep(accel_speed)
                    GPIO.output(self.stepPin1,GPIO.LOW)
                    GPIO.output(self.stepPin2,GPIO.LOW)
                    sleep(accel_speed)
                    
                #Correct steps and speed for acceleration        
                steps -= 1600
                speed = 1 / speed_max #convert frequency to seconds

            #Move at minimum speed otherwise
            else:
                speed = 1 / speed_min #convert frequency to seconds
            
            #Move the motor in the specified direction for the specified number of steps
            for step in range(steps):
                GPIO.output(self.stepPin1,GPIO.HIGH)
                GPIO.output(self.stepPin2,GPIO.HIGH)
                sleep(speed)
                GPIO.output(self.stepPin1,GPIO.LOW)
                GPIO.output(self.stepPin2,GPIO.LOW)
                sleep(speed)

        #~~~~~ Change motor direction ~~~~~
        def Motor_Direction(self,direction):
            #Change motor direction as specified
            if direction == "up":
                GPIO.output(self.dirPin1,ccw)
                GPIO.output(self.dirPin2,cw)
            elif direction == "down":
                GPIO.output(self.dirPin1,cw)
                GPIO.output(self.dirPin2,ccw)
            elif direction == "left":
                GPIO.output(self.dirPin1,ccw)
                GPIO.output(self.dirPin2,ccw)
            elif direction == "right":
                GPIO.output(self.dirPin1,cw)
                GPIO.output(self.dirPin2,cw)

        #~~~~~ Movement based on direction and distance ~~~~~
        def Move_Distance(self,direction,distance,location):
            #Change motor direction as specified
            Motor_Direction(direction)

            steps_to_move = Dist_to_Steps(distance) #number of steps to move
            dist_to_move = Steps_to_Dist(steps_to_move) #actual distance moved after rounding
            dist_to_move = distance

            #Calculate new position
            if direction == "up":
                location[1] += dist_to_move
                
                #Set the speed for movement
                speed_max = self.speed_max_default
                speed_min = self.speed_min_default
                
            elif direction == "down":
                location[1] -= dist_to_move
                
                #Set the speed for movement
                speed_max = self.speed_max_default
                speed_min = self.speed_min_default
                
            elif direction == "left":
                location[0] -= dist_to_move
                
                #Set the speed for movement
                speed_max = self.speed_max_default/2
                speed_min = self.speed_min_default/2
                
            elif direction == "right":
                location[0] += dist_to_move
                
                #Set the speed for movement
                speed_max = self.speed_max_default/2
                speed_min = self.speed_min_default/2

            #Move the motors into position
            if distance != 0:
                Move_Motors(self,steps_to_move,speed_max,speed_min)

            return location #Return the new X,Y position

        #Move to a specific position
        def Move_To(self,x_move,y_move,location):
            #Make sure values are valid first
            if x_move <= 12.0 and x_move >= 0.0 and y_move <= 45.0 and y_move >= 0.0:
                
                #Calculate relative movements to get into position
                x_move = x_move - location[0]
                y_move = y_move - location[1]

                x_move_direction = "right" if x_move > 0.0 else "left"
                y_move_direction = "up" if y_move > 0.0 else "down"
                
                #Move Y position first
                location = Move_Distance(self,y_move_direction,abs(y_move),location)
                
                sleep(0.5)
                
                #Move X position second
                location = Move_Distance(self,x_move_direction,abs(x_move),location)
                
                sleep(0.5)
                
                return location
            
            #If invlaid input
            else:
                return location
                

        #~~~~~ Zero the location (to be used later) ~~~~~
        def Zero_Motors(self):

            #Move the motors slightly in case they are already in the zero position
            Move_Distance(self,"up",2,[0,0]) #Move up 2cm
            sleep(1)
            Move_Distance(self,"right",2,[0,0]) #Move right 2cm
            sleep(1)

            #Zero the Y position first
            Motor_Direction("down")
            while(GPIO.input(self.zeroPinY) == GPIO.HIGH):
                Move_Motors(self,1,1e3,1e3) #very slowly move motors 1 step at a time
            sleep(2)

            #Zero the X position second
            Motor_Direction("left")
            while(GPIO.input(self.zeroPinX) == GPIO.HIGH):
                Move_Motors(self,1,1e3,1e3) #very slowly move motors 1 step at a time
            sleep(2)

            #Move the motors slightly off the actual zero point
            Motor_Direction("right")
            for i in range(800):
                Move_Motors(1,10e3,10e3)
            sleep(1)
            Motor_Direction("up")
            for i in range(800):
                Move_Motors(1,10e3,10e3)
            sleep(1)

            return [0,0] #return the new X,Y positon