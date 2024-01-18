# Copyright (C) 2024 HeronErin
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 3 of the
# License, or (at your option) any later version.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.



#!base C:\Users\void\Documents\example.v5python
#!out C:\Users\void\Documents\controller.v5python
#!dump partial.py



#!dump listView.py



#!ignoreNextLine
from partial import partial
from vex import *
#!ignoreNextLine
controller_1 = Controller(PRIMARY)
#!ignoreNextLine
motor_1 = Motor(Ports.PORT1, 1, False)
#!ignoreNextLine
motor_2 = Motor(Ports.PORT2, 1, False)
#!ignoreNextLine
motor_3 = Motor(Ports.PORT3, 1, False)
#!ignoreNextLine
motor_4 = Motor(Ports.PORT4, 1, False)
#!ignoreNextLine
motor_5 = Motor(Ports.PORT5, 1, False)
#!ignoreNextLine
motor_6 = Motor(Ports.PORT5, 1, False)

#!ignoreNextLine
brain=Brain()





MoterStuff = listView([
        ("#1", False),
        ("#2", False),
        ("#3", False),
        ("#4", False),
        ("#5", False),
        ("#6", False),
    ])

Menu = [
    ('Invert direction', False),
    ('Invert turning', False),
    ("Invert shoot", False),
    ("Conv speed", 7),
    ('Turn coefficient', 2),
    ("Moter directions", MoterStuff)
  ]

def moter_fix(val, index):
    return val if MoterStuff.data[index][-1] else -val


#!dump controllerScreen.py


def driver(*args):    
    m1 = controller_1.axis3.position() - (controller_1.axis4.position()/screen.baseList.get("Turn coefficient"))
    m2 = controller_1.axis3.position() + (controller_1.axis4.position()/screen.baseList.get("Turn coefficient"))
    if screen.baseList.get("Invert direction"):
        m1=-m1
        m2=-m2
    if screen.baseList.get("Invert turning"):
        m3 = m1
        m1=m2
        m2=m3
    motor_1.set_velocity(moter_fix(m1, 0)                      , PERCENT)
    motor_2.set_velocity(moter_fix(m2, 1)                      , PERCENT)
    motor_1.spin(FORWARD)
    motor_2.spin(FORWARD)
    # print(controller_1.axis4.position())

def conv_belt(*args):
    speed = controller_1.axis2.position()

    motor_3.set_velocity(moter_fix(speed, 2) * screen.baseList.get("Conv speed") / 10                    , PERCENT)
    motor_3.spin(FORWARD)

# trigRot = 0
# def spin360():
#     global trigRot
#     trigRot+=moter_fix(360, 3)
#     motor_4.spin_to_position(trigRot, DEGREES)
fireDir = True
def fire(*args):
    global fireDir
    
    if fireDir:
        # global fireDir
        fireDir=False
        motor_4.set_velocity(moter_fix(100, 3))
        motor_5.set_velocity(moter_fix(100, 4))
        # wait(1.5, SECONDS)
        motor_6.set_velocity(moter_fix(20 , 5))

        
    else:
        # global fireDir
        fireDir=True
        motor_4.set_velocity(0)
        motor_5.set_velocity(0)
        motor_6.set_velocity(0)
    motor_4.spin(REVERSE if screen.baseList.get("Invert shoot") else FORWARD )
    motor_5.spin(REVERSE if screen.baseList.get("Invert shoot") else FORWARD )
    motor_6.spin(REVERSE if screen.baseList.get("Invert shoot") else FORWARD )


def pre_autonomous():
    # actions to do when the program starts
    wait(1, SECONDS)

def autonomous():
    brain.screen.clear_screen()
    brain.screen.print("autonomous code")

screen = None
def user_control():
    global screen
    brain.screen.clear_screen()
    #!dump controllerBindings.py


# create competition instance
comp = Competition(user_control, autonomous)
pre_autonomous()














