from machine import Pin
from .mcp4725 import MCP4725

led = Pin(25, Pin.OUT)
led.toggle()

i2c=I2C(0,freq=400000,scl=Pin(21),sda=Pin(20))
dac = MCP4725(i2c,96)
dac.write(0)