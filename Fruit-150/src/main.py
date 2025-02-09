from vex import *

brain=Brain()
controller = Controller()
left_motor_front = Motor(Ports.PORT1, GearSetting.RATIO_6_1, True)
left_motor_back = Motor(Ports.PORT2, GearSetting.RATIO_6_1, True)
leftMotors = MotorGroup(left_motor_front, left_motor_back)

right_motor_front = Motor(Ports.PORT3, GearSetting.RATIO_6_1, False)
right_motor_back = Motor(Ports.PORT4, GearSetting.RATIO_6_1, False)
rightMotors = MotorGroup(right_motor_front, right_motor_back)

bedMotor = Motor(Ports.PORT5, GearSetting.RATIO_6_1, False)
rackMotor = Motor(Ports.PORT6, GearSetting.RATIO_6_1, False)
## Button handler. Note that we check the state and then act accordingly
def handleLeft1Button():
    print(controller.axis1.position(), "RIGHT X")
    print(controller.axis2.position(), "RIGHT Y")
    print(controller.axis3.position(), "LEFT Y")
    print(controller.axis4.position(), "LEXT X")

## Same as "if check button press -> handle button press"
controller.buttonL1.pressed(handleLeft1Button)

def dropBed():
    bedMotor.spin_for(FORWARD, 120, DEGREES)
def liftBed():
    bedMotor.spin_for(REVERSE, 120, DEGREES)


controller.buttonA.pressed(dropBed)
controller.buttonB.pressed(liftBed)
## Everything is event-driven through the event library...no code in the main loop!
while True:
    leftMotors.spin(FORWARD, controller.axis3.position() + controller.axis4.position(), PERCENT)
    rightMotors.spin(FORWARD, controller.axis3.position() - controller.axis4.position(), PERCENT)

    rackMotor.spin(REVERSE, controller.axis2.position() / 2, PERCENT)

