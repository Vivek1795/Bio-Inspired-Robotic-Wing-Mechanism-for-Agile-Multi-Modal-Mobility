# main.py -- put your code here!
from machine import Pin, PWM # type: ignore
from time import sleep
frequency = 50
range_low = 28
range_high = 122
servo1 = PWM(Pin(13),frequency)
while(True):
    servo1.duty(range_low)
    sleep(1)
    servo1.duty(range_high)
    sleep(2)