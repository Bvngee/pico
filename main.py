### NEWEST ATTEMPT (QWIIC python module)

from machine import I2C, Pin
from qwiic_vl53l1x import QwiicVL53L1X
import time

print("VL53L1X Qwiic Test\n")

i2c = I2C(id=0, sda=Pin(16), scl=Pin(17), freq=400000)
print(i2c.scan())
#tof = QwiicVL53L1X(i2c_driver=i2c)
tof = QwiicVL53L1X()
if (tof.sensor_init() == None):					 # Begin returns 0 on a good init
	print("Sensor online!\n")

while True:
	try:
		tof.start_ranging()						 # Write configuration bytes to initiate measurement
		time.sleep(.005)
		distance = tof.get_distance()	 # Get the result of the measurement from the sensor
		time.sleep(.005)
		tof.stop_ranging()

		print("Distance(mm): " % (distance))

	except Exception as e:
		print(e)

### NEWER ATTEMPT

# from machine import I2C, Pin
# from vl53l0x import VL53L0X
# from utime import sleep_ms
#
# i2c = I2C(id=0, sda=Pin(16), scl=Pin(17))
# vl = VL53L0X(i2c)
#
# while True:
#     print("Distance: {} cm".format(vl.range)) 
#     sleep_ms(50)

### LESS OLD ATTEMP

# from machine import Pin
# from machine import I2C
# import VL53L0X
# 
# i2c = I2C(id=0, sda=Pin(16), scl=Pin(17))
# 
# # Create a VL53L0X object
# tof = VL53L0X.VL53L0X(i2c)
# 
# tof.set_Vcsel_pulse_period(tof.vcsel_period_type[0], 18)
# 
# tof.set_Vcsel_pulse_period(tof.vcsel_period_type[1], 14)
# 
# 
# while True:
# # Start ranging
#     tof.start()
#     tof.read()
#     print(tof.read())
#     tof.stop()

###





    #q = tof.set_signal_rate_limit(0.1)
    #
    # time.sleep(0.1)


### OLD ATTEMP


# #import board
# from machine import I2C, Pin
# import vl53l4cd
#
# i2c = I2C(id=0, sda=Pin(16), scl=Pin(17))  # uses board.SCL and board.SDA
# # i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller
#
# vl53 = vl53l4cd.VL53L4CD(i2c)
#
# # OPTIONAL: can set non-default values
# vl53.inter_measurement = 0
# vl53.timing_budget = 200
#
# print("VL53L4CD Simple Test.")
# print("--------------------")
# model_id, module_type = vl53.model_info
# print("Model ID: 0x{:0X}".format(model_id))
# print("Module Type: 0x{:0X}".format(module_type))
# print("Timing Budget: {}".format(vl53.timing_budget))
# print("Inter-Measurement: {}".format(vl53.inter_measurement))
# print("--------------------")
#
# vl53.start_ranging()
#
# while True:
#     while not vl53.data_ready:
#         pass
#     vl53.clear_interrupt()
#     print("Distance: {} cm".format(vl53.distance))
