#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Maybe use following guide to make this an mqtt client?
https://www.hivemq.com/blog/mqtt-client-library-paho-python
'''

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_temperature import BrickletTemperature
import time

HOST = "192.168.63.183"
PORT = 4223
UID = "e2q"

if __name__ == "__main__":
    ipcon = IPConnection()
    t = BrickletTemperature(UID, ipcon)

    ipcon.connect(HOST, PORT)

    try:
        while True:
            temperature = t.get_temperature()
            print("Temperature: " + str(temperature/100.0) + " °C")
            time.sleep(1)
    except KeyboardInterrupt:
        print('Checking temperature end.')

    ipcon.disconnect()
