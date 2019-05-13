"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Displays the Graphical User Interface (GUI) and communicates with the robot.

  Authors:  Your professors (for the framework)
    and Micah Fletcher.
  Spring term, 2018-2019.
"""
# DONE 1:  Put your name in the above.

import tkinter
from tkinter import ttk

import mqtt_remote_method_calls as mqtt
import m1_laptop_code as m1
import m3_laptop_code as m3


def get_my_frame(root, window, mqtt_sender):
    # Construct your frame:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame_label = ttk.Label(frame, text="Micah Fletcher")
    frame_label.grid()
    # DONE 2: Put your name in the above.

    # Add the rest of your GUI to your frame:
    # TODO: Put your GUI onto your frame (using sub-frames if you wish).
    spin_left_button = ttk.Button(frame, text="spin left")

    spin_right_button = ttk.Button(frame, text='spin right')

    speed_label = ttk.Label(frame, text="Enter Speed below")
    speed_entry_box = ttk.Entry(frame, width=10)
    speed_entry_box.insert(0, '100')

    degrees_label = ttk.Label(frame, text="Enter Degrees below")
    degrees_entry_box = ttk.Entry(frame, width=10)
    degrees_entry_box.insert(0, '0')

    spin_left_button.grid()
    spin_right_button.grid()
    speed_entry_box.grid()
    degrees_entry_box.grid()

    spin_left_button['command'] = lambda: handle_spin_left(speed_entry_box,
                                                           degrees_entry_box,
                                                           mqtt_sender)
    spin_right_button['command'] = lambda: handle_spin_right(
        speed_entry_box, degrees_entry_box, mqtt_sender)

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

def handle_spin_left(speed_entry_box, degrees_entry_box, mqtt_sender):
    print("handle_spin_left: ", speed_entry_box.get(), degrees_entry_box.get())
    speed = int(speed_entry_box.get())
    degrees = int(degrees_entry_box.get())
    mqtt_sender.send_message("spin_left", [speed, degrees])


def handle_spin_right(speed_entry_box, degrees_entry_box, mqtt_sender):
    print("handle_spin_right: ", speed_entry_box.get(),
          degrees_entry_box.get())
    speed = int(speed_entry_box.get())
    degrees = int(degrees_entry_box.get())
    mqtt_sender.send_message("spin_right", [speed, degrees])
