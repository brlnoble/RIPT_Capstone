import PySimpleGUI as sg
import RPi.GPIO as GPIO
from time import sleep

################################################################################################################################################
################################ Setup #########################################################################################################

#Define the stepper motor pins
dirPin1 = 1 #CHANGE ME
stepPin1 = 1 #CHANGE ME

dirPin2 = 2 #CHANGE ME
stepPin2 = 2 #CHANGE ME

#Define the zeroing pins
zeroPinX = 3 #ignore for now
zeroPinY = 3 #ignore for now

#Setup the GPIO pins
GPIO.setmode(GPIO.BCM)

GPIO.setup(dirPin1,GPIO.OUT)
GPIO.setup(stepPin1,GPIO.OUT)
GPIO.setup(dirPin2,GPIO.OUT)
GPIO.setup(stepPin2,GPIO.OUT)

GPIO.setup(zeroPinX,GPIO.IN)
GPIO.setup(zeroPinY,GPIO.IN)

################################################################################################################################################
############################## Move Motors #####################################################################################################

def MoveMotor(direction,pulseDelay,waitDelay):
    #Select motor direction
    if direction == "up":
        GPIO.output(dirPin1,GPIO.LOW)
        GPIO.output(dirPin2,GPIO.HIGH)
    elif direction == "down":
        GPIO.output(dirPin1,GPIO.HIGH)
        GPIO.output(dirPin2,GPIO.LOW)
    elif direction == "left":
        GPIO.output(dirPin1,GPIO.LOW)
        GPIO.output(dirPin2,GPIO.LOW)
    elif direction == "right":
        GPIO.output(dirPin1,GPIO.HIGH)
        GPIO.output(dirPin2,GPIO.HIGH)

    #Move one step
    GPIO.output(stepPin1,GPIO.HIGH)
    GPIO.output(stepPin2,GPIO.HIGH)
    sleep(pulseDelay)
    GPIO.output(stepPin1,GPIO.LOW)
    GPIO.output(stepPin2,GPIO.LOW)
    sleep(pulseDelay)


################################################################################################################################################
################################ Interface #####################################################################################################


sg.theme('DefaultNoMoreNagging')
sg.theme_text_element_background_color(color = '#EEE')
sg.theme_text_color('#1D2873')
sg.theme_background_color('#EEE')

font = ('Arial', 16)
btn_font = ('Arial', 16, 'bold')

layout = [ 
            [sg.Text("Hold a button to move the motor in that direction.",font=font)],
            [sg.Text("Pulse delay is time between pulses, time delay is time between movements.",font=font)],
            [sg.RealtimeButton("UP",key="up",font=btn_font,size=(10,2))],
            [sg.RealtimeButton("LEFT",key="left",font=btn_font,size=(10,2)),sg.RealtimeButton("RIGHT",key="right",font=btn_font,size=(10,2))],
            [sg.RealtimeButton("DOWN",key="down",font=btn_font,size=(10,2))],
            [sg.Text()],
            [sg.Text("Pulse delay (s): "),sg.Input(key="p_delay",font=font,enable_events=True,size=(20,2))],
            [sg.Text("Time delay (s): "),sg.Input(key="t_delay",font=font,enable_events=True,size=(20,2))],
            [sg.Text()],
            [sg.Text("",font=font,size=(10,2),key="status")],
            [sg.Text()],
            [sg.Button("Exit",key="exit",font=btn_font,size=(10,2),button_color="red")]
]

window = sg.Window("Motor Move Input", layout, element_justification="c", finalize=True)

#Default values
window["p_delay"].update(value="0.5")
window["t_delay"].update(value="2")

while True:
    event,values = window.read(timeout=0) #read in all the values and events

    if event in (sg.WINDOW_CLOSED, sg.TITLEBAR_CLOSE_KEY, "exit",):
        break

    #If user hits submit
    if event != sg.TIMEOUT_EVENT:
        window["status"].update(event)
        MoveMotor(event,values["p_delay"],values["t_delay"])
    else:
        window["status"].update("")
    

window.close() #Close the program