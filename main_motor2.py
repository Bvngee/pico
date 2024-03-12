from machine import Pin, PWM
from time import sleep
from adafruit_motor.motor import DCMotor, SLOW_DECAY

freq = 20000
motor_a_1 = PWM(Pin(0), freq=freq)
motor_a_2 = PWM(Pin(1), freq=freq)
motor_b_1 = PWM(Pin(2), freq=freq)
motor_b_2 = PWM(Pin(3), freq=freq)
motor_a = DCMotor(motor_a_1, motor_a_2)
motor_b = DCMotor(motor_b_1, motor_b_2)

motor_a.decay_mode = SLOW_DECAY
motor_b.decay_mode = SLOW_DECAY

motor_a.throttle = 1.0
motor_b.throttle = 1.0
sleep(1)
motor_a.throttle = None
motor_b.throttle = None
sleep(1)
motor_a.throttle = -1.0
motor_b.throttle = -1.0
sleep(1)
motor_a.throttle = None
motor_b.throttle = None
