import RPi.GPIO as GPIO #for IO control
from time import sleep #for delay functionality
import PySimpleGUI as sg #for simple interface

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Setup ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Define the stepper motor pins
dirPin1 = 21 #direction pin for motor 1
stepPin1 = 20 #pulse pin for motor 1

dirPin2 = 6 #direction pin for motor 2
stepPin2 = 5 #pulse pin for motor 2

#Define the zeroing pins
zeroPinX = 3
zeroPinY = 3

#Parameters of the motors
p_delay = 0.00001 #delay between pulses (40k Hz default)
m_delay = 0.5 #delay between movements
m_steps = 1600 #steps per rotation (1/8 microstep)
m_diameter = 1.215 #diameter of the motor gear in cm

#Location tracking
x_location = 0
y_location = 0

#Setup the GPIO pins
GPIO.setmode(GPIO.BCM)

GPIO.setup(dirPin1,GPIO.OUT)
GPIO.setup(stepPin1,GPIO.OUT)
GPIO.setup(dirPin2,GPIO.OUT)
GPIO.setup(stepPin2,GPIO.OUT)

GPIO.setup(zeroPinX,GPIO.IN)
GPIO.setup(zeroPinY,GPIO.IN)

#Define clockwise and counter clockwise for readability
cw = GPIO.HIGH
ccw = GPIO.LOW

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Functions ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~ Convert cm to steps ~~~~~
def Dist_to_Steps(distance):
    return int( (distance / (3.14156 * m_diameter)) * m_steps) #return the number of steps as an integer

#~~~~~ Convert steps to cm ~~~~~
def Steps_to_Dist(steps):
    return (steps / m_steps) * (3.14156 * m_diameter)
    
#~~~~~ Move motors a given number of steps ~~~~~
def Move_Motors(steps,speed):
    
    #Move the motor in the specified direction for the specified number of steps
    for step in range(steps):
        GPIO.output(stepPin1,GPIO.HIGH)
        GPIO.output(stepPin2,GPIO.HIGH)
        sleep(speed)
        GPIO.output(stepPin1,GPIO.LOW)
        GPIO.output(stepPin2,GPIO.LOW)
        sleep(speed)

#~~~~~ Change motor direction ~~~~~
def Motor_Direction(direction):
    #Change motor direction as specified
    if direction == "up":
        GPIO.output(dirPin1,ccw)
        GPIO.output(dirPin2,cw)
    elif direction == "down":
        GPIO.output(dirPin1,cw)
        GPIO.output(dirPin2,ccw)
    elif direction == "left":
        GPIO.output(dirPin1,ccw)
        GPIO.output(dirPin2,ccw)
    elif direction == "right":
        GPIO.output(dirPin1,cw)
        GPIO.output(dirPin2,cw)

#~~~~~ Movement based on direction and distance ~~~~~
def Move_Distance(direction,distance,x_pos,y_pos):

    #Change motor direction as specified
    Motor_Direction(direction)

    steps_to_move = Dist_to_Steps(distance) #number of steps to move
    dist_to_move = Steps_to_Dist(steps_to_move) #actual distance moved after rounding

    #Calculate new position
    if direction == "up":
        y_pos += dist_to_move
    elif direction == "down":
        y_pos -= dist_to_move
    elif direction == "left":
        x_pos -= dist_to_move
    elif direction == "right":
        x_pos += dist_to_move

    #Move the motors into position
    if distance != 0:
        Move_Motors(steps_to_move,p_delay)
        
        print("\tSteps: " + str(steps_to_move))
        print("\tDist: " + str(dist_to_move))
        print("\tAcc: " + str(100 * (dist_to_move - distance) / distance) + "%")

    return (x_pos, y_pos) #Return the new X,Y position

#~~~~~ Zero the location (to be used later) ~~~~~
def Zero_Motors():

    #Move the motors slightly in case they are already in the zero position
    Move_Distance("up",2) #Move up 2cm
    Move_Distance("right",2) #Move right 2cm

    #Zero the Y position first
    while(GPIO.read(zeroPinY) == 0):
        Move_Motors(1,p_delay*100) #very slowly move motors 1 step at a time

    #Zero the X position second
    while(GPIO.read(zeroPinX) == 0):
        Move_Motors(1,p_delay*100) #very slowly move motors 1 step at a time

    return (0,0) #return the new X,Y positon

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ GUI Setup ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Window theme
sg.theme('DefaultNoMoreNagging')
sg.theme_text_element_background_color(color = '#EEE')
sg.theme_text_color('#1D2873')
sg.theme_background_color('#EEE')

font = ('Arial', 16)
btn_font = ('Arial', 16, 'bold')

#Layout and elements
hbot = b"iVBORw0KGgoAAAANSUhEUgAAAJYAAADICAYAAAAKhRhlAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAACxMAAAsTAQCanBgAAAcyaVRYdFhNTDpjb20uYWRvYmUueG1wAAAAAAA8P3hwYWNrZXQgYmVnaW49Iu+7vyIgaWQ9Ilc1TTBNcENlaGlIenJlU3pOVGN6a2M5ZCI/PiA8eDp4bXBtZXRhIHhtbG5zOng9ImFkb2JlOm5zOm1ldGEvIiB4OnhtcHRrPSJBZG9iZSBYTVAgQ29yZSA2LjAtYzAwMiA3OS4xNjQzNTIsIDIwMjAvMDEvMzAtMTU6NTA6MzggICAgICAgICI+IDxyZGY6UkRGIHhtbG5zOnJkZj0iaHR0cDovL3d3dy53My5vcmcvMTk5OS8wMi8yMi1yZGYtc3ludGF4LW5zIyI+IDxyZGY6RGVzY3JpcHRpb24gcmRmOmFib3V0PSIiIHhtbG5zOnhtcD0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wLyIgeG1sbnM6eG1wTU09Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9tbS8iIHhtbG5zOnN0RXZ0PSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvc1R5cGUvUmVzb3VyY2VFdmVudCMiIHhtbG5zOnBob3Rvc2hvcD0iaHR0cDovL25zLmFkb2JlLmNvbS9waG90b3Nob3AvMS4wLyIgeG1sbnM6ZGM9Imh0dHA6Ly9wdXJsLm9yZy9kYy9lbGVtZW50cy8xLjEvIiB4bXA6Q3JlYXRvclRvb2w9IkFkb2JlIFBob3Rvc2hvcCAyMS4xIChXaW5kb3dzKSIgeG1wOkNyZWF0ZURhdGU9IjIwMjMtMDEtMjlUMDk6MTI6MzAtMDU6MDAiIHhtcDpNZXRhZGF0YURhdGU9IjIwMjMtMDEtMjlUMDk6MTI6MzAtMDU6MDAiIHhtcDpNb2RpZnlEYXRlPSIyMDIzLTAxLTI5VDA5OjEyOjMwLTA1OjAwIiB4bXBNTTpJbnN0YW5jZUlEPSJ4bXAuaWlkOjFiZGM0ZWRjLTgxM2EtYWE0OC1iOTZlLWMyOWFmYTYxMzhhYSIgeG1wTU06RG9jdW1lbnRJRD0iYWRvYmU6ZG9jaWQ6cGhvdG9zaG9wOmY3Yzk3NTgyLThkYTEtMTU0YS1iZmVkLWIzMTVhZTJkMzZiNyIgeG1wTU06T3JpZ2luYWxEb2N1bWVudElEPSJ4bXAuZGlkOjAyYmYzODI1LWJlZmQtMzg0MS1hNTBlLTM1ZmFhYTcxZmM0MiIgcGhvdG9zaG9wOkNvbG9yTW9kZT0iMyIgZGM6Zm9ybWF0PSJpbWFnZS9wbmciPiA8eG1wTU06SGlzdG9yeT4gPHJkZjpTZXE+IDxyZGY6bGkgc3RFdnQ6YWN0aW9uPSJjcmVhdGVkIiBzdEV2dDppbnN0YW5jZUlEPSJ4bXAuaWlkOjAyYmYzODI1LWJlZmQtMzg0MS1hNTBlLTM1ZmFhYTcxZmM0MiIgc3RFdnQ6d2hlbj0iMjAyMy0wMS0yOVQwOToxMjozMC0wNTowMCIgc3RFdnQ6c29mdHdhcmVBZ2VudD0iQWRvYmUgUGhvdG9zaG9wIDIxLjEgKFdpbmRvd3MpIi8+IDxyZGY6bGkgc3RFdnQ6YWN0aW9uPSJzYXZlZCIgc3RFdnQ6aW5zdGFuY2VJRD0ieG1wLmlpZDoxYmRjNGVkYy04MTNhLWFhNDgtYjk2ZS1jMjlhZmE2MTM4YWEiIHN0RXZ0OndoZW49IjIwMjMtMDEtMjlUMDk6MTI6MzAtMDU6MDAiIHN0RXZ0OnNvZnR3YXJlQWdlbnQ9IkFkb2JlIFBob3Rvc2hvcCAyMS4xIChXaW5kb3dzKSIgc3RFdnQ6Y2hhbmdlZD0iLyIvPiA8L3JkZjpTZXE+IDwveG1wTU06SGlzdG9yeT4gPHBob3Rvc2hvcDpUZXh0TGF5ZXJzPiA8cmRmOkJhZz4gPHJkZjpsaSBwaG90b3Nob3A6TGF5ZXJOYW1lPSJIIiBwaG90b3Nob3A6TGF5ZXJUZXh0PSJIIi8+IDxyZGY6bGkgcGhvdG9zaG9wOkxheWVyTmFtZT0iMSIgcGhvdG9zaG9wOkxheWVyVGV4dD0iMSIvPiA8cmRmOmxpIHBob3Rvc2hvcDpMYXllck5hbWU9IjIiIHBob3Rvc2hvcDpMYXllclRleHQ9IjIiLz4gPHJkZjpsaSBwaG90b3Nob3A6TGF5ZXJOYW1lPSIrWSIgcGhvdG9zaG9wOkxheWVyVGV4dD0iK1kiLz4gPHJkZjpsaSBwaG90b3Nob3A6TGF5ZXJO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"

layout = [
    [sg.Text("Input the distance to be moved, and select the direction.",font=font)],
    [sg.Text("Distance in cm: ",font=btn_font),sg.Input("0",key="dist_move",enable_events=True,size=(5,1))],
    [sg.Text()],
    
    [sg.Column(
        [
            [sg.VPush()],
            [sg.Button("Left",key="move_left",font=btn_font,button_color='#02AB29',size=(5,1))],
            [sg.VPush()],
        ],element_justification='c'
    ),

    sg.Column(
        [
            [sg.Button("Up",key="move_up",font=btn_font,button_color='#F5AC11',size=(5,1))],
            [sg.Image(hbot,pad=(0,0))],
            [sg.Button("Down",key="move_down",font=btn_font,button_color='#F5AC11',size=(5,1))],
        ],element_justification='c'
    ),

    sg.Column(
        [
            [sg.VPush()],
            [sg.Button("Right",key="move_right",font=btn_font,button_color='#02AB29',size=(5,1))],
            [sg.VPush()],
        ],element_justification='c'
    )],

    [sg.Text("",font=font,key="info")],
    [sg.Button("Exit",key="close_program_btn",font=btn_font,button_color='#F5273A',size=(10,1))]
]

window = sg.Window('Movement Test',layout,element_justification='c',finalize=True)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Main Loop ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

while True:
    event, values = window.read(timeout=100)

    #If user closes the window
    if event in (sg.WINDOW_CLOSED,"close_program_btn"):
        break

    #Move based on what user inputs
    if event in ("move_up","move_down","move_left","move_right"):
        if values["dist_move"] != "":
            print("Moving " + str(event[5:]))
            
            x_location,y_location = Move_Distance(event[5:],float(values["dist_move"]),x_location,y_location)
            
            print("X: " + str(x_location))
            print("Y: " + str(y_location))
            print("")
            
            window["dist_move"].update(value="0")

#Program closed, clear everything
window.close()
GPIO.cleanup()
