#Blinks an LED connected to the Pico via Pin 15

from machine import Pin

led = Pin(15, Pin.OUT)
led.value(1)
