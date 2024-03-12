from machine import Pin
from time import sleep
print('hi')

led = Pin("LED")
p0 = Pin(0, Pin.OUT)
p1 = Pin(1, Pin.OUT)
p2 = Pin(2, Pin.OUT)
p3 = Pin(3, Pin.OUT)

led.on()
sleep(1)
led.off()

p0.off()
p2.off()
p1.on()
p3.on()

sleep(2)

led.on()
sleep(1)
led.off()

p0.on()
p2.on()
p1.off()
p3.off()
