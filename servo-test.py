from gpiozero import AngularServo
from time import sleep

bot_serv = AngularServo(12, min_angle = 0, max_angle = 270, min_pulse_width = 0.0005, max_pulse_width = 0.0025)
top_serv = AngularServo(13, min_angle = 0, max_angle = 270, min_pulse_width = 0.0005, max_pulse_width = 0.0025)

#from arduin0
# for top servo 
# jab = 90 
# uppercut & hook = 10
# for bottom servo 
# jab & uppercut = 125 
# hook = 30

def jab(bot_serv, top_serv):
    bot_serv.angle = 180
    top_serv.angle = 225
    sleep(2)
    return 0

def uppercut(bot_serv, top_serv):
    bot_serv.angle = 180
    top_serv.angle = 180
    sleep(2)
    return 0

def hook(bot_serv, top_serv):
    bot_serv.angle = 50
    top_serv.angle = 180
    sleep(2)
    return 0

while 1:
    jab(bot_serv, top_serv)
    uppercut(bot_serv, top_serv)
    hook(bot_serv, top_serv)
