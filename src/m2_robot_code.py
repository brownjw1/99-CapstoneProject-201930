"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  Author:  Your professors (for the framework)
    and Micah Fletcher.
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

    def stop(self):
        """ Tells the robot to stop moving. """
        print_message_received("stop")
        self.robot.drive_system.stop()

    # TODO: Add methods here as needed.
    def spin_left(self, speed, degrees):
        """spins the robot to the left."""
        print('turn left')
        self.robot.drive_system.right_motor.turn_on(speed)
        self.robot.drive_system.left_motor.turn_on((-speed))
        while True:
            if self.robot.drive_system.right_motor.get_position() / 5.5 >= \
                    degrees:
                self.robot.drive_system.right_motor.turn_off()
                self.robot.drive_system.left_motor.turn_off()
                self.robot.drive_system.right_motor.reset_position()
                break

    def spin_right(self, speed, degrees):
        """spins the robot to the left."""
        print('turn right')
        self.robot.drive_system.right_motor.turn_on(-speed)
        self.robot.drive_system.left_motor.turn_on(speed)
        while True:
            print('in while loop')
            if self.robot.drive_system.right_motor.get_position() / 5.5 <= \
                    -degrees:
                self.robot.drive_system.right_motor.turn_off()
                self.robot.drive_system.left_motor.turn_off()
                self.robot.drive_system.right_motor.reset_position()
                break

    def spin_until_facing(self, signature, x, delta, speed):
        """spins the robot to the right."""
        print('testing spin until')
        while True:
            print('in while loop')
            if self.robot.sensor_system.camera.get_biggest_blob().center.x > \
                    x + delta:
                print('turn left until', self.robot.sensor_system.camera
                      .get_biggest_blob().center.x,
                      (x - delta))
                self.robot.drive_system.right_motor.turn_on(speed)
                self.robot.drive_system.left_motor.turn_on((-speed))


            elif self.robot.sensor_system.camera.get_biggest_blob().center.x \
                    < x - delta:
                print('turn right until',
                      self.robot.sensor_system.camera.get_biggest_blob().center.x,
                      (x + delta))
                self.robot.drive_system.right_motor.turn_on(-speed)
                self.robot.drive_system.left_motor.turn_on(speed)


            else:
                self.robot.drive_system.right_motor.turn_off()
                self.robot.drive_system.left_motor.turn_off()
                break


def print_message_received(method_name, arguments=None):
    print()
    print("The robot's delegate has received a message")
    print("for the  ", method_name, "  method, with arguments", arguments)

# TODO: Add functions here as needed.
