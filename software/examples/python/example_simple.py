#!/usr/bin/env python
# -*- coding: utf-8 -*-  

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change to your UID

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_tilt import Tilt

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    tilt = Tilt(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Get current tilt state
    tilt_state = tilt.get_tilt_state()

    if tilt_state == Tilt.TILT_STATE_CLOSED:
        print('closed')
    elif tilt_state == Tilt.TILT_STATE_OPEN:
        print('open')
    elif tilt_state == Tilt.TILT_STATE_CLOSED_VIBRATING:
        print('closed vibrating')

    raw_input('Press key to exit\n') # Use input() in Python 3
    ipcon.disconnect()
