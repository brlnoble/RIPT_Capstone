import RPi.GPIO as GPIO
from time import sleep

class servo:
    def __init__(self, pin):
        self.pin = pin

    def SetGPIO(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pin, GPIO.OUT)

    def SetAngle(self, angle): 
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
top_serv.SetGPIO()

# for top servo jab = 90 uppercut & hook = 10, for bottom servo jab & uppercut = 125, hook = 30

def jab():
    bot_serv.SetAngle(125)
    top_serv.SetAngle(90)
def uppercut():
    bot_serv.SetAngle(125) 
    top_serv.SetAngle(10)
def hook():
    bot_serv.SetAngle(30) 
    top_serv.SetAngle(10)

i = 0
while i<25:
    jab()
    sleep(1)
    uppercut()
    sleep(1)
    hook()
    sleep(1)
    i += 1

GPIO.cleanup()
