import RPi.GPIO as GPIO
from time import sleep

class servo:
    def __init__(self, pin):
        self.pin = pin

    def SetGPIO(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pin, GPIO.OUT)

    def SetAngle(self, angle): #could write different positions into this function or could set the positions as defined properties of the class
        pwm=GPIO.PWM(self.pin, 50)
        pwm.start(0)
        duty = angle / 18 + 2
        GPIO.output(self.pin, True)
        pwm.ChangeDutyCycle(duty)
        sleep(1)
        GPIO.output(self.pin, False)
        pwm.ChangeDutyCycle(0)
        pwm.stop()


bot_serv = servo(03)
top_serv = servo(04)

bot_serv.SetGPIO()
bot_serv.SetAngle(90) #need to figure out the angles
top_serv.SetGPIO() #only need to set GPIO pins at the start
top_serv.SetAngle(90) 


GPIO.cleanup()
