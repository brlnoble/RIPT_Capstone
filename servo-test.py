import RPi.GPIO as GPIO
from time import sleep

bot_serv = 12
top_serv = 13
bot_pos = 125
top_pos = 90

GPIO.setmode(GPIO.BOARD)
GPIO.setup(bot_serv, GPIO.OUT)
GPIO.setup(top_serv, GPIO.OUT)

# for top servo 
# jab = 90 
# uppercut & hook = 10
# for bottom servo 
# jab & uppercut = 125 
# hook = 30

def jab(bot_serv, top_serv, bot_pos, top_pos):
    if bot_pos == 125:
        pwm_bot=GPIO.PWM(bot_serv, 50)
        pwm_bot.start(0)
        duty_bot = bot_pos / 18 + 2
        GPIO.output(bot_serv, True)
        pwm_bot.ChangeDutyCycle(duty_bot)
        sleep(1)
        GPIO.output(bot_serv, False)
        pwm_bot.ChangeDutyCycle(0)
        pwm_bot.stop()
    else:
        bot_pos = 125
        pwm_bot=GPIO.PWM(bot_serv, 50)
        pwm_bot.start(0)
        duty_bot = bot_pos / 18 + 2
        GPIO.output(bot_serv, True)
        pwm_bot.ChangeDutyCycle(duty_bot)
        sleep(1)
        GPIO.output(bot_serv, False)
        pwm_bot.ChangeDutyCycle(0)
        pwm_bot.stop()
    if top_pos == 90:
        pwm_top=GPIO.PWM(top_serv, 50)
        pwm_top.start(0)
        duty_top = top_pos / 18 + 2
        GPIO.output(top_serv, True)
        pwm_top.ChangeDutyCycle(duty_top)
        sleep(1)
        GPIO.output(top_serv, False)
        pwm_top.ChangeDutyCycle(0)
        pwm_top.stop()
    else:
        top_pos = 90
        pwm_top=GPIO.PWM(top_serv, 50)
        pwm_top.start(0)
        duty_top = top_pos / 18 + 2
        GPIO.output(top_serv, True)
        pwm_top.ChangeDutyCycle(duty_top)
        sleep(1)
        GPIO.output(top_serv, False)
        pwm_top.ChangeDutyCycle(0)
        pwm_top.stop()

def uppercut(bot_serv, top_serv, bot_pos, top_pos):
    if bot_pos == 125:
        pwm_bot=GPIO.PWM(bot_serv, 50)
        pwm_bot.start(0)
        duty_bot = bot_pos / 18 + 2
        GPIO.output(bot_serv, True)
        pwm_bot.ChangeDutyCycle(duty_bot)
        sleep(1)
        GPIO.output(bot_serv, False)
        pwm_bot.ChangeDutyCycle(0)
        pwm_bot.stop()
    else:
        bot_pos = 125
        pwm_bot=GPIO.PWM(bot_serv, 50)
        pwm_bot.start(0)
        duty_bot = bot_pos / 18 + 2
        GPIO.output(bot_serv, True)
        pwm_bot.ChangeDutyCycle(duty_bot)
        sleep(1)
        GPIO.output(bot_serv, False)
        pwm_bot.ChangeDutyCycle(0)
        pwm_bot.stop()
    if top_pos == 10:
        pwm_top=GPIO.PWM(top_serv, 50)
        pwm_top.start(0)
        duty_top = top_pos / 18 + 2
        GPIO.output(top_serv, True)
        pwm_top.ChangeDutyCycle(duty_top)
        sleep(1)
        GPIO.output(top_serv, False)
        pwm_top.ChangeDutyCycle(0)
        pwm_top.stop()
    else:
        top_pos = 10
        pwm_top=GPIO.PWM(top_serv, 50)
        pwm_top.start(0)
        duty_top = top_pos / 18 + 2
        GPIO.output(top_serv, True)
        pwm_top.ChangeDutyCycle(duty_top)
        sleep(1)
        GPIO.output(top_serv, False)
        pwm_top.ChangeDutyCycle(0)
        pwm_top.stop()

def hook(bot_serv, top_serv, bot_pos, top_pos):
    if bot_pos == 30:
        pwm_bot=GPIO.PWM(bot_serv, 50)
        pwm_bot.start(0)
        duty_bot = bot_pos / 18 + 2
        GPIO.output(bot_serv, True)
        pwm_bot.ChangeDutyCycle(duty_bot)
        sleep(1)
        GPIO.output(bot_serv, False)
        pwm_bot.ChangeDutyCycle(0)
        pwm_bot.stop()
    else:
        bot_pos = 30
        pwm_bot=GPIO.PWM(bot_serv, 50)
        pwm_bot.start(0)
        duty_bot = bot_pos / 18 + 2
        GPIO.output(bot_serv, True)
        pwm_bot.ChangeDutyCycle(duty_bot)
        sleep(1)
        GPIO.output(bot_serv, False)
        pwm_bot.ChangeDutyCycle(0)
        pwm_bot.stop()
    if top_pos == 10:
        pwm_top=GPIO.PWM(top_serv, 50)
        pwm_top.start(0)
        duty_top = top_pos / 18 + 2
        GPIO.output(top_serv, True)
        pwm_top.ChangeDutyCycle(duty_top)
        sleep(1)
        GPIO.output(top_serv, False)
        pwm_top.ChangeDutyCycle(0)
        pwm_top.stop()
    else:
        top_pos = 10
        pwm_top=GPIO.PWM(top_serv, 50)
        pwm_top.start(0)
        duty_top = top_pos / 18 + 2
        GPIO.output(top_serv, True)
        pwm_top.ChangeDutyCycle(duty_top)
        sleep(1)
        GPIO.output(top_serv, False)
        pwm_top.ChangeDutyCycle(0)
        pwm_top.stop()

i = 0
while i<25:
    jab(bot_serv, top_serv, bot_pos, top_pos)
    sleep(1)
    uppercut(bot_serv, top_serv, bot_pos, top_pos)
    sleep(1)
    hook(bot_serv, top_serv, bot_pos, top_pos)
    sleep(1)
    i += 1

GPIO.cleanup()
