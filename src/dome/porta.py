#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

def abrir ():

	servo = 5

	GPIO.setmode(GPIO.BOARD)

	GPIO.setup(servo,GPIO.OUT)

	p=GPIO.PWM(servo,50)# 50hz frequency

	p.start(2.5)# starting duty cycle ( it set the servo to 0 degree )


	try:
		p.ChangeDutyCycle(11)
	        time.sleep(2)

	        p.ChangeDutyCycle(3)
		time.sleep(1)
		p.start(2.5)

	except KeyboardInterrupt:
		GPIO.cleanup()
	finally:
		GPIO.cleanup()
abrir()
