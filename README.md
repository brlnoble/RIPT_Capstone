# R.I.P.T. Capstone Project
This is a final year engineering capstone project for McMaster University. Students were given 8 months to develop a project and then present to judges and supervisors.
Work is currently in progress, with an anticipated end date of April 1st, 2023.

___

## About the Project
The **Robot Integrated Pad Trainer** (R.I.P.T.) is a device for helping boxers develop their offensive skills. The project uses a YOLOv7 computer vision model to observe and track the user with webcams, and identifies deficiencies in their skills. Once a training regime has been developed by a custom algorithm, pad training sessions can be conducted with the new regime. A gantry like system moves pads around for the user to interact with, sensing when they are hit before moving to a new location. This robotic emulation of a human pad trainer allows for more direct customization in the training, and is expandable and repeatable for any number of users and skill levels.

This project is a collaboration between Brandon Noble ([brlnoble](https://github.com/brlnoble "Brandon's Github")), Labib Kazi ([kazia3](https://github.com/kazia3 "Labib's Github")), Jame Tran ([JameTran](https://github.com/JameTran "Jame's Github")), and Hunter Ceranic ([cer-hunter](https://github.com/cer-hunter "Hunter's Github")).

___

## Project Goals
- [ ] Robotic system to control boxing training pads
  - [X] H-bot inspired pulley system with 10mm GT2 belt, and custom mounts
  - [X] Zero motor position
  - [ ] Fine motor control for NEMA 24 stepper motors to accurately move gantry system to specific locations
- [ ] System to change pad orientation along 2 axes
  - [ ] Mechanical design to support pad
  - [ ] Control over position for different types of punches
- [ ] YOLOv7 computer vision model
  - [X] Train YOLOv7 tiny model to recognize faces and boxing gloves
  - [X] Deploy on NVIDIA Jetson Nano
  - [X] Determine user blocking with intersection between gloves and face
  - [ ] Identify different punches based on movements (i.e. jab, cross, uppercut, etc.)
- [ ] Display and collect user metrics
  - [ ] Implement various sensors to collect user metrics (i.e. reaction time, speed, endurance, accuracy, etc.)
  - [ ] Web application to display metrics and training sessions
  
___

## Current State
The project is very much a work in progress and is actively changing day to day. Below are some images and videos of the current state. More detailed images and pictures to come.

#### Movement Test of H-Bot System
<img src="https://github.com/brlnoble/RIPT_Capstone/blob/main/Pictures%20and%20Documents/Movement_Test_Jan20.gif" width="200"> <img src="https://github.com/brlnoble/RIPT_Capstone/blob/main/Pictures%20and%20Documents/Movement_Test_Jan29.gif" width="200">
<img src="https://github.com/brlnoble/RIPT_Capstone/blob/main/Pictures%20and%20Documents/Zeroing_Test.gif" width="900">
<img src="https://github.com/brlnoble/RIPT_Capstone/blob/main/Pictures%20and%20Documents/Movement_Test_Feb19.gif" width="900">

#### Pad Orientation and Control
<img src="https://github.com/brlnoble/RIPT_Capstone/blob/main/Pictures%20and%20Documents/Pad_Orient_1.gif" width="200"> <img src="https://github.com/brlnoble/RIPT_Capstone/blob/main/Pictures%20and%20Documents/Pad_Orient_2.gif" width="200">

#### CAD of One Side of the Device
<img src="https://github.com/brlnoble/RIPT_Capstone/blob/main/Pictures%20and%20Documents/One_Side_Model.jpg" width="900">

#### Selfie with our YOLOv7 Model
<img src="https://github.com/brlnoble/RIPT_Capstone/blob/main/Pictures%20and%20Documents/YOLO_Selfie.jpg" width="450">
