try:
  import usocket as socket
except:
  import socket

from machine import Pin
import network

import esp
esp.osdebug(None)

import gc
gc.collect()

ssid = '<WIFI-SSID>'
password = '<PASSWORD>'

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

#Turn on the led if a valid connection to network has established
top_led = Pin(2, Pin.OUT)
top_led.on()

while station.isconnected() == False:
  pass

top_led.off()
print('Connection successful')
print(station.ifconfig())

