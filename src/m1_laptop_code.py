"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Displays the Graphical User Interface (GUI) and communicates with the robot.

  Authors:  Your professors (for the framework)
    and Jared Brown.
  Spring term, 2018-2019.
"""
# DONE 1:  Put your name in the above.

import tkinter
from tkinter import ttk

import mqtt_remote_method_calls as mqtt
import m2_laptop_code as m2
import m3_laptop_code as m3


def get_my_frame(root, window, mqtt_sender):
    # Construct your frame:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame_label = ttk.Label(frame, text="Jared Brown")
    frame_label.grid()
    # DONE 2: Put your name in the above.

    # Add the rest of your GUI to your frame:
    # TODO: Put your GUI onto your frame (using sub-frames if you wish).
    forward_button = ttk.Button(frame, text="Go Forward")
    backward_button = ttk.Button(frame, text="Go Backward")
    speed_Entry = ttk.Entry(frame,width=8)
    speed_Entry.insert(0,100)
    distance_Entry = ttk.Entry(frame,width=8)
    distance_Entry.insert(1,100)
    delta_Entry = ttk.Entry(frame,width=8)
    delta_Entry.insert(2,100)
    go_until_button = ttk.Button(frame, text="Go Until")



    forward_button.grid()
    backward_button.grid()
    speed_Entry.grid()
    distance_Entry.grid()
    go_until_button.grid()
    delta_Entry.grid()

    forward_button["command"] = lambda: handle_forward(
        speed_Entry, distance_Entry, mqtt_sender)
    backward_button["command"] = lambda: handle_backward(
        speed_Entry, distance_Entry, mqtt_sender)
    go_until_button['command']=lambda: handle_move_until(
        speed_Entry,distance_Entry,delta_Entry,mqtt_sender)



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
def handle_forward(speed_Entry,distance_Entry,mqtt_sender):
    speed=int(speed_Entry.get())
    distance = int(distance_Entry.get())
    mqtt_sender.send_message("move_forward",[speed,distance])

def handle_backward(speed_Entry,distance_Entry,mqtt_sender):
    speed=int(speed_Entry.get())*-1
    distance = int(distance_Entry.get())
    mqtt_sender.send_message("move_backward",[speed,distance])


def handle_move_until(speed_Entry,distance_Entry,delta_Entry,mqtt_sender):
    speed=int(speed_Entry.get())
    distance=int(distance_Entry.get())
    delta=int(delta_Entry.get())
    mqtt_sender.send_message('move_until',[distance,delta,speed])


