from machine import Pin, PWM
from utime import sleep
import utime

MAX_DUTY_CYCLE = 65535
MIN_DUTY_CYCLE = 0

frequency = 100000

motor_a_pin1 = PWM(Pin(0, mode=Pin.OUT))
motor_a_pin2 = PWM(Pin(1, mode=Pin.OUT))
motor_b_pin1 = PWM(Pin(2, mode=Pin.OUT))
motor_b_pin2 = PWM(Pin(3, mode=Pin.OUT))

motor_a_pin1.freq(frequency)
motor_a_pin2.freq(frequency)
motor_b_pin1.freq(frequency)
motor_b_pin2.freq(frequency)

current_speed = MAX_DUTY_CYCLE
    
def move_forward():
    motor_a_pin1.duty_u16(current_speed)
    motor_a_pin2.duty_u16(MIN_DUTY_CYCLE)
    motor_b_pin1.duty_u16(current_speed)
    motor_b_pin2.duty_u16(MIN_DUTY_CYCLE)
       
def move_backward():
    motor_a_pin1.duty_u16(MIN_DUTY_CYCLE)
    motor_a_pin2.duty_u16(current_speed)
    motor_b_pin1.duty_u16(MIN_DUTY_CYCLE)
    motor_b_pin2.duty_u16(current_speed)

# def turn_left():
#     left_motor_pin1.duty_u16(current_speed)
#     left_motor_pin2.duty_u16(MIN_DUTY_CYCLE)
#     # right_motor_pin1.duty_u16(MAX_DUTY_CYCLE)
#     # right_motor_pin2.duty_u16(MAX_DUTY_CYCLE)
#
# def turn_right():
#     left_motor_pin1.duty_u16(MAX_DUTY_CYCLE)
#     left_motor_pin2.duty_u16(MAX_DUTY_CYCLE)
#     # right_motor_pin1.duty_u16(current_speed)
#     # right_motor_pin2.duty_u16(MIN_DUTY_CYCLE)
    
def stop():
    motor_a_pin1.duty_u16(MIN_DUTY_CYCLE)
    motor_a_pin2.duty_u16(MIN_DUTY_CYCLE)
    motor_b_pin1.duty_u16(MIN_DUTY_CYCLE)
    motor_b_pin2.duty_u16(MIN_DUTY_CYCLE)
    
''' Map duty cycle values from 0-100 to duty cycle 40000-65535 '''
def __map_range(x, in_min, in_max, out_min, out_max):
  return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min
    
''' new_speed is a value from 0% - 100% '''
def change_speed(new_speed):
    new_duty_cycle = __map_range(new_speed, 0, 100, 40000, 65535)
    current_speed = new_duty_cycle

    
def deinit():
    """deinit PWM Pins"""
    stop()
    utime.sleep(0.1)
    motor_a_pin1.deinit()
    motor_a_pin2.deinit()
    motor_b_pin1.deinit()
    motor_b_pin2.deinit()


try:
    print("hi")
    move_forward()
    sleep(1.5)
    stop()
    sleep(1.5)
    move_backward()
    sleep(2)
    deinit()
except KeyboardInterrupt:
    deinit()

