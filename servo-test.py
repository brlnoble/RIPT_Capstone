from gpiozero import AngularServo
from time import sleep

bot_serv = AngularServo(5, min_angle = 0, max_angle = 270, min_pulse_width = 0.0005, max_pulse_width = 0.0025)
top_serv = AngularServo(6, min_angle = 0, max_angle = 270, min_pulse_width = 0.0005, max_pulse_width = 0.0025)

def jab_right(bot_serv, top_serv):
    bot_serv.angle = 180
    top_serv.angle = 270
    sleep(10)
    return 0

def uppercut_right(bot_serv, top_serv):
    bot_serv.angle = 180
    top_serv.angle = 180
    sleep(10)
    return 0

def hook_right(bot_serv, top_serv):
    bot_serv.angle = 50
    top_serv.angle = 180
    sleep(10)
    return 0

def jab_left(bot_serv, top_serv):
    bot_serv.angle = 180
    top_serv.angle = 270
    sleep(10)
    return 0

def uppercut_left(bot_serv, top_serv):
    bot_serv.angle = 180
    top_serv.angle = 180
    sleep(10)
    return 0

def hook_left(bot_serv, top_serv):
    bot_serv.angle = 50
    top_serv.angle = 180
    sleep(10)
    return 0

while 1:
    jab_right(bot_serv, top_serv)
    uppercut_right(bot_serv, top_serv)
    hook_right(bot_serv, top_serv)
