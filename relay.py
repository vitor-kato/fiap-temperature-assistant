#!/usr/bin/env python3

import RPi.GPIO as GPIO
from time import sleep


def switch_relay(force_off=False):
    RELAIS_1_GPIO = 17
    GPIO.setmode(GPIO.BCM) # GPIO Numbers instead of board numbers
    GPIO.setup(RELAIS_1_GPIO, GPIO.OUT) # GPIO Assign mode

    # Determines if relay is on or off
    if GPIO.input(RELAIS_1_GPIO) and not force_off:
        GPIO.output(RELAIS_1_GPIO, GPIO.LOW) # on
    else:
        GPIO.output(RELAIS_1_GPIO, GPIO.HIGH) # off


if __name__ == "__main__":
    try:
        switch_relay()
        sleep(5)
        switch_relay()
    except:
        switch_relay(True)
        GPIO.cleanup()
