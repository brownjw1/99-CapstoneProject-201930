"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  Author:  Your professors (for the framework)
    and Jared Brown.
  Spring term, 2018-2019.
"""
# DONE 1:  Put your name in the above.

import mqtt_remote_method_calls as mqtt
import rosebot
import m2_robot_code as m2
import m3_robot_code as m3


class MyRobotDelegate(object):
    """
    Defines methods that are called by the MQTT listener when that listener
    gets a message (name of the method, plus its arguments)
    from a LAPTOP via MQTT.
    """
    def __init__(self, robot):
        self.robot = robot  # type: rosebot.RoseBot
        self.mqtt_sender = None  # type: mqtt.MqttClient
        self.is_time_to_quit = False  # Set this to True to exit the robot code

    def set_mqtt_sender(self, mqtt_sender):
        self.mqtt_sender = mqtt_sender

    def go(self, left_motor_speed, right_motor_speed):
        """ Tells the robot to go (i.e. move) using the given motor speeds. """
        print_message_received("go", [left_motor_speed, right_motor_speed])
        self.robot.drive_system.go(left_motor_speed, right_motor_speed)

    def move_forward(self,speed,distance):
        '''Moves the robot forward a specified distance'''
        degree_distance=distance/self.robot.drive_system.wheel_circumference*360
        print_message_received("go_forward",[speed,distance])
        self.robot.drive_system.right_motor.turn_on(speed)
        self.robot.drive_system.left_motor.turn_on(speed)
        while True:
            if self.robot.drive_system.left_motor.get_position()>=degree_distance:
                self.robot.drive_system.stop()
                self.robot.drive_system.left_motor.reset_position()
                self.robot.drive_system.right_motor.reset_position()
                break

    def move_backward(self,speed,distance):
        '''Moves the robot forward a specified distance'''
        degree_distance=distance/self.robot.drive_system.wheel_circumference*-360
        print_message_received("go_backward",[speed,distance])
        self.robot.drive_system.right_motor.turn_on(speed)
        self.robot.drive_system.left_motor.turn_on(speed)
        while True:
            if self.robot.drive_system.left_motor.get_position()<=degree_distance:
                self.robot.drive_system.stop()
                self.robot.drive_system.left_motor.reset_position()
                self.robot.drive_system.right_motor.reset_position()
                break



    def move_until(self,distance,delta,speed):
        print_message_received("go_until", [distance, delta, speed])
        self.robot.drive_system.right_motor.turn_on(speed)
        self.robot.drive_system.left_motor.turn_on(speed)
        def get_reading():
            reading=0
            list=[]
            largest=0
            smallest=100
            for i in range(5):
                list+=[int(self.robot.sensor_system.ir_proximity_sensor.get_distance())]
                if(list[i])>largest:
                    largest=list[i]
                if list[i]<smallest:
                    smallest=list[i]
            list.remove(largest)
            list.remove(smallest)
            for k in range(len(list)):
                reading+=list[k]
            print(reading )
            return (reading / len(list))
        while True:
            reading=get_reading()
            if reading<=distance+delta and reading>=distance-delta:
                self.robot.drive_system.stop()
                break




    # TODO: Add methods here as needed.


def print_message_received(method_name, arguments):
    print()
    print("The robot's delegate has received a message")
    print("for the  ", method_name, "  method, with arguments", arguments)


# TODO: Add functions here as needed.

