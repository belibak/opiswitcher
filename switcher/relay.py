#!/usr/bin/env python3
import random

from time import sleep

import OPi.GPIO as GPIO

class Switch:
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    def __init__(self, pin):
        self.pin = pin
        GPIO.setup(pin, GPIO.OUT)

    def test(self):
        GPIO.setup(self.pin, GPIO.OUT)        # Relay swithing on, when setups out
        sleep(0.3)
        GPIO.output(self.pin, 1)              # 1 - relay is swithed off, 0 - swithed on
        sleep(0.3)
        GPIO.cleanup(self.pin)

    def on(self):
        #GPIO.setup(pin, GPIO.OUT)        # Relay swithing on, when setups out
        GPIO.output(self.pin, 0)

    def off(self):
        #GPIO.setup(pin, GPIO.OUT)        # Relay swithing on, when setups out
        GPIO.output(self.pin, 1)  # 1 - relay is swithed off, 0 - swithed on

    def get_state(self):
        state = GPIO.input(self.pin)
        return state     # Returns 0 when relay switched on




if __name__ == "__main__":
    s = Switch(26)
    s.on()
    print(s.get_state(26))
    sleep(2)
    s.off()