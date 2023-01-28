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

def MoveMotor(numStepsX, numStepsY,pulseDelay,waitDelay):
    #Move the motors up?
    GPIO.output(dirPin1,GPIO.LOW)
    GPIO.output(dirPin2,GPIO.HIGH)
    print("Moving up (1: LOW, 2: HIGH)")

    for Y in range(0,numStepsY):
        GPIO.output(stepPin1,GPIO.HIGH)
        GPIO.output(stepPin2,GPIO.HIGH)
        sleep(pulseDelay)
        GPIO.output(stepPin1,GPIO.LOW)
        GPIO.output(stepPin2,GPIO.LOW)
        sleep(pulseDelay)
    sleep(waitDelay)

    #Move the motor left?
    GPIO.output(dirPin1,GPIO.LOW)
    GPIO.output(dirPin2,GPIO.LOW)
    print("Moving up (1: LOW, 2: LOW)")

    for X in range(0,numStepsX):
        GPIO.output(stepPin1,GPIO.HIGH)
        GPIO.output(stepPin2,GPIO.HIGH)
        sleep(pulseDelay)
        GPIO.output(stepPin1,GPIO.LOW)
        GPIO.output(stepPin2,GPIO.LOW)
        sleep(pulseDelay)
    sleep(waitDelay)

    #Move the motors down?
    GPIO.output(dirPin1,GPIO.HIGH)
    GPIO.output(dirPin2,GPIO.LOW)
    print("Moving down (1: HIGH, 2: LOW)")

    for Y in range(0,numStepsY):
        GPIO.output(stepPin1,GPIO.HIGH)
        GPIO.output(stepPin2,GPIO.HIGH)
        sleep(pulseDelay)
        GPIO.output(stepPin1,GPIO.LOW)
        GPIO.output(stepPin2,GPIO.LOW)
        sleep(pulseDelay)
    sleep(waitDelay)

    #Move the motor right?
    GPIO.output(dirPin1,GPIO.HIGH)
    GPIO.output(dirPin2,GPIO.HIGH)
    print("Moving right (1: HIGH, 2: HIGH)")

    for X in range(0,numStepsX):
        GPIO.output(stepPin1,GPIO.HIGH)
        GPIO.output(stepPin2,GPIO.HIGH)
        sleep(pulseDelay)
        GPIO.output(stepPin1,GPIO.LOW)
        GPIO.output(stepPin2,GPIO.LOW)
        sleep(pulseDelay)
    sleep(waitDelay)

    print("Finished")


################################################################################################################################################
################################ Interface #####################################################################################################


sg.theme('DefaultNoMoreNagging')
sg.theme_text_element_background_color(color = '#EEE')
sg.theme_text_color('#1D2873')
sg.theme_background_color('#EEE')

font = ('Arial', 16)
btn_font = ('Arial', 16, 'bold')

layout = [ 
            [sg.Text("Input the number of steps to move each motor.",font=font)],
            [sg.Text("Pulse delay is time between pulses, time delay is time between movements.",font=font)],
            [sg.Text("X Steps:"),sg.Input(key="x_steps",font=font,enable_events=True,size=(20,2))],
            [sg.Text("Y Steps:"),sg.Input(key="y_steps",font=font,enable_events=True,size=(20,2))],
            [sg.Text()],
            [sg.Text("Pulse delay (s): "),sg.Input(key="p_delay",font=font,enable_events=True,size=(20,2))],
            [sg.Text("Time delay (s): "),sg.Input(key="t_delay",font=font,enable_events=True,size=(20,2))],
            [sg.Text()],
            [sg.Button("Submit",key="submit",font=btn_font,size=(20,2)),sg.Button("Exit",key="exit",font=btn_font,size=(10,2),button_color="red")]
]

window = sg.Window("Motor Move Input", layout, element_justification="c", finalize=True)

#Default values
window["p_delay"].update(value="0.5")
window["t_delay"].update(value="2")

while True:
    windows,event,values = sg.read_all_windows(timeout=100) #read in all the values and events

    if event in (sg.WINDOW_CLOSED, sg.TITLEBAR_CLOSE_KEY, "exit",):
        break

    #If user hits submit
    if event == "submit":
        if values["x_steps"].lstrip("-+").isdigit() and values["y_steps"].lstrip("-+").isdigit(): #make sure only integers
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~')
            print("X: " + str(values["x_steps"]))
            print("Y: " + str(values["y_steps"]))
            #MoveMotor(int(values["x_steps"]),int(values["y_steps"]))
        else:
            sg.popup("Invalid input")
    

window.close() #Close the program