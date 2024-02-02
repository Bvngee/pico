from machine import Pin, PWM
from utime import sleep, sleep_ms

servo_freq = 20
continuous_servo_pwm = PWM(Pin(0), freq=servo_freq)

led = Pin("LED", Pin.OUT)
ina1 = Pin(18, Pin.OUT)
ina2 = Pin(17, Pin.OUT)
pwma = PWM(Pin(16))
pwma.freq(1000)

led.value(0)
sleep(0.6)
led.value(1)


def RotateCW(duty):
    ina1.value(1)
    ina2.value(0)
    duty_16 = int((duty*65536)/100)
    pwma.duty_u16(duty_16)

def RotateCCW(duty):
    ina1.value(0)
    ina2.value(1)
    duty_16 = int((duty*65536)/100)
    pwma.duty_u16(duty_16)
    
def StopMotor():
    ina1.value(0)
    ina2.value(0)
    pwma.duty_u16(0)
    

def RotateServoCW():
    continuous_servo_pwm.duty_u16(round((0.7/servo_freq) * 65536))

def RotateServoCCW():
    continuous_servo_pwm.duty_u16(round((2.3/servo_freq) * 65536))

def StopServoMotor():
    continuous_servo_pwm.duty_u16(round((1.5/servo_freq) * 65536))


duty_cycle = 500
while ...:
    # RotateCW(duty_cycle)
    # sleep(3)
    # StopMotor()
    # RotateCCW(duty_cycle)
    # sleep(3)
    # StopMotor()

    RotateServoCW()
    sleep(3)
    StopServoMotor()
    sleep(3)
    RotateServoCCW()
    sleep(3)
    StopServoMotor()
    sleep(3)




### ULTRASONIC SENSOR CODE ###

# SOUND_SPEED=340 
# TRIG_PULSE_DURATION_US=10
#
# trig_pin = Pin(15, Pin.OUT) 
# echo_pin = Pin(14, Pin.IN)  
#
# while True:
#
#     trig_pin.value(0)
#     time.sleep_us(5)
#
#     trig_pin.value(1)
#     time.sleep_us(TRIG_PULSE_DURATION_US)
#     trig_pin.value(0)
#
#     ultrason_duration = time_pulse_us(echo_pin, 1, 30000) 
#     distance_mm = 10 * SOUND_SPEED * ultrason_duration / 20000
#
#     print(f"Distance : {distance_mm} mm")
#     time.sleep_ms(500)
