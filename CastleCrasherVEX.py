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
    direct = 0
    global myVariable
    while True:
        if front_eye.near_object() or down_eye.detect(RED) or left_bumper.pressed():
            drivetrain.drive_for(REVERSE, 30, MM)
            if down_eye.detect(RED):
                while down_eye.detect(RED):
                    direct = drivetrain.turn_for(LEFT, 10, DEGREES)
            else:
                drivetrain.turn_for(LEFT, r.randint(1,180), DEGREES)
            print(direct)

        if front_eye.near_object() or down_eye.detect(RED) or right_bumper.pressed():
            drivetrain.drive_for(REVERSE, 30, MM)
            if down_eye.detect(RED):
                while down_eye.detect(RED):
                    direct = drivetrain.turn_for(RIGHT, 10, DEGREES)
            else:
                drivetrain.turn_for(RIGHT, r.randint(1,180), DEGREES)

            print(direct)




        while (not front_eye.near_object() and not left_bumper.pressed() and not right_bumper.pressed() and not down_eye.detect(RED)):
            drivetrain.drive(FORWARD)
            wait(5, MSEC)
        wait(5, MSEC)

vr_thread(when_started1)
