#!/usr/bin/env python

import RPi.GPIO as GPIO
import SimpleMFRC522

def leer ():

	reader = SimpleMFRC522.SimpleMFRC522()

	try:
		id, text = reader.read()
		return("%s" % id)
	finally:
		GPIO.cleanup()
