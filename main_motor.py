from machine import Pin, PWM
from utime import sleep
import utime

MAX_DUTY_CYCLE = 65535
MIN_DUTY_CYCLE = 0

motor_pins = [16, 17]
frequency = 100

left_motor_pin1 = PWM(Pin(motor_pins[0], mode=Pin.OUT))
left_motor_pin2 = PWM(Pin(motor_pins[1], mode=Pin.OUT))
# right_motor_pin1 = PWM(Pin(motor_pins[2], mode=Pin.OUT))
# right_motor_pin2 = PWM(Pin(motor_pins[3], mode=Pin.OUT))

left_motor_pin1.freq(frequency)
left_motor_pin2.freq(frequency)
# right_motor_pin1.freq(frequency)
# right_motor_pin2.freq(frequency)

current_speed = MAX_DUTY_CYCLE
    
def move_forward():
    left_motor_pin1.duty_u16(current_speed)
    left_motor_pin2.duty_u16(MIN_DUTY_CYCLE)
    # right_motor_pin1.duty_u16(current_speed)
    # right_motor_pin2.duty_u16(MIN_DUTY_CYCLE)
       
def move_backward():
    left_motor_pin1.duty_u16(MIN_DUTY_CYCLE)
    left_motor_pin2.duty_u16(current_speed)
    # right_motor_pin1.duty_u16(MIN_DUTY_CYCLE)
    # right_motor_pin2.duty_u16(current_speed)
    
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
    left_motor_pin1.duty_u16(MIN_DUTY_CYCLE)
    left_motor_pin2.duty_u16(MIN_DUTY_CYCLE)
    # right_motor_pin1.duty_u16(MIN_DUTY_CYCLE)
    # right_motor_pin2.duty_u16(MIN_DUTY_CYCLE)
    
''' Map duty cycle values from 0-100 to duty cycle 40000-65535 '''
def __map_range(x, in_min, in_max, out_min, out_max):
  return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min
    
''' new_speed is a value from 0% - 100% '''
def change_speed(new_speed):
    new_duty_cycle = __map_range(new_speed, 0, 100, 40000, 65535)
    current_speed = new_duty_cycle

    
def deinit():
    """deinit PWM Pins"""
    print("Deinitializing PWM Pins")
    stop()
    utime.sleep(0.1)
    left_motor_pin1.deinit()
    left_motor_pin2.deinit()
    # right_motor_pin1.deinit()
    # right_motor_pin2.deinit()


try:
    print("hi")
    move_forward()
    sleep(2)
    move_backward()
    sleep(2)
    deinit()
except KeyboardInterrupt:
    deinit()

