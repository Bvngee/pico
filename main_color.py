from machine import Pin, I2C
from time import sleep
from adafruit_as726x import AS726x_I2C

i2c = I2C(id=0, scl=Pin(1), sda=Pin(0))
print(i2c.scan())
print("hi")
as726x = AS726x_I2C(i2c_bus=i2c)
print("hi2")
print(as726x.temperature)
# as726x.indicator_led = True
# as726x.driver_led = True

as726x.conversion_mode = as726x.MODE_2

def graph_map(x):
    return min(int(x * 80 / 16000), 80)

# while True:
# Wait for data to be ready
# while not as726x.data_ready:
#     sleep(0.1)
#     print("(no data yet)")

print("\n")
print("V: " + graph_map(as726x.violet) * "=")
print("B: " + graph_map(as726x.blue) * "=")
print("G: " + graph_map(as726x.green) * "=")
print("Y: " + graph_map(as726x.yellow) * "=")
print("O: " + graph_map(as726x.orange) * "=")
print("R: " + graph_map(as726x.red) * "=")
sleep(0.5)
