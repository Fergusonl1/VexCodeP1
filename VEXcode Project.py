#region VEXcode Generated Robot Configuration
import math
import random
from vexcode import *

drivetrain = Drivetrain()
magnet = Electromagnet("magnet", 0)
pen = Pen()
brain = Brain()
left_bumper = Bumper("leftBumper", 1)
right_bumper = Bumper("rightBumper", 2)
distance = Distance()
front_eye = EyeSensor("fronteye", 3)
down_eye = EyeSensor("downeye", 4)
location = Location()

#endregion VEXcode Generated Robot Configuration
myVariable = 0
import random as r

def when_started1():
    global myVariable
    drivetrain.drive_for(FORWARD, 200, MM)
    drivetrain.turn_for(RIGHT, 90, DEGREES)
    drivetrain.drive_for(FORWARD, 400, MM)
    wait(1, SECONDS)
    while True:
        if distance.found_object():
            drivetrain.turn_for(LEFT, random.randint(1,359), DEGREES)
        else:
            drivetrain.turn_for(RIGHT, random.randint(1,359), DEGREES)
        wait(0.5, SECONDS)
        while not front_eye.near_object() or not distance.found_object():
            drivetrain.drive(FORWARD)
            wait(0, MSEC)
        wait(5, MSEC)

vr_thread(when_started1)
