from machine import Pin
from time import sleep, localtime

led = Pin(15, mode=Pin.OUT)

dht = DHT11(Pin(17, mode=Pin.OUT, pull=Pin.PULL_DOWN))

f = open("log.txt", "a")
f.write("----- start ------")

while True:
    try:
        sleep(0.25)
        dht.measure()
        line = "\ntime: " + str(localtime())
            + " temp: " + str(dht.temperature())
            + " humidity: " + str(dht.humidity())
        f.write(line)
        if dht.humidity() > 50:
            led.on()
        else:
            led.off()
    except KeyboardInterrupt:
        print("exited")
        break
    except:
        print("error reading")

f.close()
