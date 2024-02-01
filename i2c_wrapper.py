from machine import I2C

class I2C_Wrapper(I2C):
    def __init__(self, i2c: I2C, device_address: int) -> None:
        I2C.__init__(i2c)
        self.device_address = device_address

    def unlock(self):

    def try_lock(self):


