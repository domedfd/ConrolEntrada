import time
import RPi.GPIO as gpio

gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)
gpio.setup(23,gpio.OUT)

try:
    while True:
        	gpio.output(23,0)
        	time.sleep(0.3)
        	gpio.output(23,1)
       		time.sleep(0.3)
except KeyboardInterrupt:
            gpio.cleanup()
            exit
