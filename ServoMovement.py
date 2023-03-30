from gpiozero import AngularServo
from time import sleep
import RPi.GPIO as GPIO

class RIPT_Servo:
    def __init__(self,servoPins,strAngs,upAngs,hookAngs):
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(servoPins[0],GPIO.OUT)
        GPIO.setup(servoPins[1],GPIO.OUT)
        
        self.top_serv = GPIO.PWM(servoPins[0],50)#AngularServo(servoPins[0], min_angle = 0, max_angle = 270, min_pulse_width = 0.0005, max_pulse_width = 0.0025)
        self.bot_serv = GPIO.PWM(servoPins[1],50)#AngularServo(servoPins[1], min_angle = 0, max_angle = 270, min_pulse_width = 0.0005, max_pulse_width = 0.0025)
        
        self.top_serv.start(0)
        self.bot_serv.start(0)
        
        self.strTop = strAngs[0]
        self.strBot = strAngs[1]
        
        self.upTop = upAngs[0]
        self.upBot = upAngs[1]
        
        self.hookTop = hookAngs[0]
        self.hookBot = hookAngs[1]
        
    
    def convert_angle(self,angle):
        return 2+angle/18
    
    def straight(self):
        self.top_serv.ChangeDutyCycle(self.convert_angle(self.strTop))
        self.bot_serv.ChangeDutyCycle(self.convert_angle(self.strBot))
        return 0

    def uppercut(self):
        self.top_serv.ChangeDutyCycle(self.convert_angle(self.upTop))
        self.bot_serv.ChangeDutyCycle(self.convert_angle(self.upBot))
        return 0

    def hook(self):
        self.top_serv.ChangeDutyCycle(self.convert_angle(self.hookTop))
        self.bot_serv.ChangeDutyCycle(self.convert_angle(self.hookBot))
        return 0

    def move_servo(self,movement):
        print(movement)
        if movement == "straight":
            self.straight()
        elif movement == "uppercut":
            self.uppercut()
        else:
            self.hook()
