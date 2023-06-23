# R.I.P.T. Capstone Project
This is a final year engineering capstone project for McMaster University. Students were given 8 months to develop a project and then present to judges and supervisors.

🏅3rd place for Most Impressive Prototype.

___

## About the Project
The **Robot Integrated Pad Trainer** (R.I.P.T.) is a device for helping boxers develop their offensive skills. The project uses a YOLOv7 computer vision model to observe and track the user with webcams, and identifies deficiencies in their skills. Once a training regime has been developed by a custom algorithm, pad training sessions can be conducted with the new regime. A gantry like system moves pads around for the user to interact with, sensing when they are hit before moving to a new location. This robotic emulation of a human pad trainer allows for more direct customization in the training, and is expandable and repeatable for any number of users and skill levels.

This project is a collaboration between Brandon Noble ([brlnoble](https://github.com/brlnoble "Brandon's Github")), Labib Kazi ([kazia3](https://github.com/kazia3 "Labib's Github")), Jame Tran ([JameTran](https://github.com/JameTran "Jame's Github")), and Hunter Ceranic ([cer-hunter](https://github.com/cer-hunter "Hunter's Github")).

### Explanation and Demonstration
View the explanation on YouTube <a href="https://youtu.be/TRa0bQ9WmGY" target="_blank" rel="noopener noreferrer">here</a>

View the demonstration on YouTube <a href="https://youtu.be/QMfrOVIuLZo" target="_blank" rel="noopener noreferrer">here</a>

___

## Project Goals
- [X] Robotic system to control boxing training pads
  - [X] H-bot inspired pulley system with 10mm GT2 belt, and custom mounts
  - [X] Zero motor position
  - [X] Fine motor control for NEMA 24 stepper motors to accurately move gantry system to specific locations
- [X] System to change pad orientation along 2 axes
  - [X] Mechanical design to support pad
  - [X] Control over position for different types of punches
- [X] YOLOv7 computer vision model
  - [X] Train YOLOv7 tiny model to recognize faces and boxing gloves
  - [X] Deploy on NVIDIA Jetson Nano
  - [X] Determine user blocking with intersection between gloves and face
- [X] Display and collect user metrics
  - [X] Implement various sensors to collect user metrics (i.e. reaction time, speed, endurance, accuracy, etc.)
  - [X] Web application to display metrics and training sessions
  - [X] Utilize user metrics to personalize a training regime
  
___

## Current State
The project is completed and almost all of the original goals have been met. Below are some pictures and GIFs of the device in operation.

#### Operation of the Device
<img src="https://github.com/brlnoble/RIPT_Capstone/blob/main/Pictures%20and%20Documents/Movement_Final_Face_On.gif" width="900">
<img src="https://github.com/brlnoble/RIPT_Capstone/blob/main/Pictures%20and%20Documents/Movement_Final_Side.gif" width="900">

#### 3D Model of the Future of RIPT
<img src="https://github.com/brlnoble/RIPT_Capstone/blob/main/Pictures%20and%20Documents/RIPT_Future.png" width="900">

### Front End Demonstration of the Web App
<img src="https://github.com/brlnoble/RIPT_Capstone/blob/main/Pictures%20and%20Documents/Web_Front_End_Mar6.gif" width="900">
You can view a function version of the website at https://brlnoble.github.io/RIPT_Capstone/

#### Demonstration of the YOLOv7 Model
<img src="https://github.com/brlnoble/RIPT_Capstone/blob/main/Pictures%20and%20Documents/YOLO_Selfie.jpg" width="450">
<img src="https://github.com/brlnoble/RIPT_Capstone/blob/main/Pictures%20and%20Documents/YOLO_Final.gif" width="900">
<img src="https://github.com/brlnoble/RIPT_Capstone/blob/main/Pictures%20and%20Documents/YOLO_Screen.gif" width="900">
