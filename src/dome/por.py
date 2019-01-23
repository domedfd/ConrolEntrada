#!/usr/bin/env python
import RPi.GPIO as GPIO
import time


def abrir ():
        channel = 21
        canal = 20

        # GPIO setup
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(channel, GPIO.OUT)
        GPIO.setup(canal, GPIO.OUT)

        def motor_on(pin, pin2):
            GPIO.output(pin, GPIO.HIGH)  # Turn motor on
            GPIO.output(pin2, GPIO.LOW)


        def motor_off(pin, pin2):
            GPIO.output(pin, GPIO.LOW)  # Turn motor off
            GPIO.output(pin2, GPIO.HIGH)  # Turn motor off

        try:
                motor_off(channel, canal)
                time.sleep(2)
                motor_on(channel, canal)
        except KeyboardInterrupt:
                GPIO.cleanup()
abrir()
