#Turns on the onboard LED of the Pi Pico

from machine import Pin

led = Pin(25, Pin.OUT)
led.value(1)
