from machine import Pin, PWM
from time import sleep
from adafruit_motor.motor import DCMotor, SLOW_DECAY

freq = 20000
pin1 = PWM(Pin(16), freq=freq)
pin2 = PWM(Pin(17), freq=freq)
motor = DCMotor(pin1, pin2)

motor.decay_mode = SLOW_DECAY
motor.throttle = 1.0
sleep(1)
motor.throttle = -1.0
sleep(1)
motor.throttle = None
