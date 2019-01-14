import RPi.GPIO as GPIO
import time

control = [2.5,3,4,5,6,7,8,9,11,11,11,11.8]

servo = 3

GPIO.setmode(GPIO.BOARD)

GPIO.setup(servo,GPIO.OUT)
# in servo motor,
# 1ms pulse for 0 degree (LEFT)
# 1.5ms pulse for 90 degree (MIDDLE)
# 2ms pulse for 180 degree (RIGHT)

# so for 50hz, one frequency is 20ms
# duty cycle for 0 degree = (1/20)*100 = 5%
# duty cycle for 90 degree = (1.5/20)*100 = 7.5%
# duty cycle for 180 degree = (2/20)*100 = 10%

p=GPIO.PWM(servo,50)# 50hz frequency

p.start(2.5)# starting duty cycle ( it set the servo to 0 degree )


try:
       while True:
           for x in range(11):
             p.ChangeDutyCycle(control[11])
             time.sleep(0.09)
             print 11
           
           for x in range(9,0,-1):
             p.ChangeDutyCycle(control[0])
             time.sleep(0.09)
             print 0
           
except KeyboardInterrupt:
    GPIO.cleanup()
