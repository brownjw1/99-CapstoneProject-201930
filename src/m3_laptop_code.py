"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Displays the Graphical User Interface (GUI) and communicates with the robot.

  Authors:  Your professors (for the framework)
    and Maria Bruner.
  Spring term, 2018-2019.
"""
# DONE:  Put your name in the above.

import tkinter
from tkinter import ttk

import mqtt_remote_method_calls as mqtt
import m1_laptop_code as m1
import m2_laptop_code as m2


def get_my_frame(root, window, mqtt_sender):
    # Construct your frame:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame_label = ttk.Label(frame, text="Maria Bruner")
    frame_label.grid()
    # DONE 2: Put your name in the above.

    # Add the rest of your GUI to your frame:
    # TODO: Put your GUI onto your frame (using sub-frames if you wish).
    arm_up_button = ttk.Button(frame, text="Arm up")
    speed_entry_box = ttk.Entry(frame, width=8)
    speed_entry_box.insert(0, "100")
    arm_down_button = ttk.Button(frame, text="Arm down")
    arm_calibrate_button = ttk.Button(frame, text="Calibrate")
    arm_to_button = ttk.Button(frame, text="Arm to 'X'")
    arm_to_entry_box = ttk.Entry(frame, width=10)
    arm_to_entry_box.insert(0, "0")
    color_entry_box = ttk.Entry(frame, width=8)
    color_entry_box.insert(0, "color")
    go_until_color_button = ttk.Button(frame, text="Go until color")

    speed_entry_box.grid()
    arm_up_button.grid()
    arm_down_button.grid()
    arm_calibrate_button.grid()
    arm_to_entry_box.grid()
    arm_to_button.grid()
    color_entry_box.grid()
    go_until_color_button.grid()

    arm_up_button['command'] = lambda: handle_arm_up(speed_entry_box, mqtt_sender)
    arm_down_button['command'] = lambda: handle_arm_down(speed_entry_box, mqtt_sender)
    arm_calibrate_button['command'] = lambda: handle_calibrate(speed_entry_box, mqtt_sender)
    arm_to_button['command'] = lambda: handle_arm_to(speed_entry_box, arm_to_entry_box, mqtt_sender)
    go_until_color_button['command'] = lambda: handle_go_until_color(speed_entry_box, color_entry_box, mqtt_sender)

    # Return your frame:
    return frame


class MyLaptopDelegate(object):
    """
    Defines methods that are called by the MQTT listener when that listener
    gets a message (name of the method, plus its arguments)
    from the ROBOT via MQTT.
    """
    def __init__(self, root):
        self.root = root  # type: tkinter.Tk
        self.mqtt_sender = None  # type: mqtt.MqttClient

    def set_mqtt_sender(self, mqtt_sender):
        self.mqtt_sender = mqtt_sender

    # TODO: Add methods here as needed.


# TODO: Add functions here as needed.
def handle_arm_up(speed_entry_box, mqtt_sender):
    print("handle_arm_up: ", speed_entry_box.get())
    speed = int(speed_entry_box.get())
    mqtt_sender.send_message("arm_up", [speed])


def handle_arm_down(speed_entry_box, mqtt_sender):
    print("handle_arm_down: ", speed_entry_box.get())
    speed = int(speed_entry_box.get())
    mqtt_sender.send_message("arm_down", [speed])


def handle_calibrate(speed_entry_box, mqtt_sender):
    print("handle_calibrate:", speed_entry_box.get())
    speed = int(speed_entry_box.get())
    mqtt_sender.send_message("arm_calibrate", [speed])


def handle_arm_to(speed_entry_box, arm_to_entry_box, mqtt_sender):
    print("handle_arm_to:", speed_entry_box.get())
    speed = int(speed_entry_box.get())
    location = int(arm_to_entry_box.get())
    mqtt_sender.send_message("arm_to", [speed, location])


def handle_go_until_color(speed_entry_box, color_entry_box, mqtt_sender):
    print("handle_go_until_color:", color_entry_box.get(), speed_entry_box.get())
    color = str(color_entry_box.get())
    speed = int(speed_entry_box.get())
    mqtt_sender.send_message("go_until_color", [color, speed])
