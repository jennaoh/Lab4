import RPi.GPIO as GPIO #import RPi.GPIO module
import time

led_pin=18

def init():
    GPIO.setmode(GPIO.BCM) #choose BCM mode
    GPIO.setwarnings(False)
    GPIO.setup(22,GPIO.IN) #set GPIO 22 as input
    GPIO.setup(18,GPIO.OUT)


def read_slide_switch():
    ret = 0

    if GPIO.input(22):
        ret = 1

    return ret

def LED_Blink():
    if read_slide_switch==1:
        for i in range(50):
            GPIO.output(18,1)
            time.sleep(0.1)
            GPIO.output(18,0)
            time.sleep(0.1)

