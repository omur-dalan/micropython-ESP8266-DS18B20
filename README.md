# micropython-ESP8266-DS18B20
Advertising Temperature Data from DS18B20 with micropython on ESP8266 (NodeMCU)

## Requirement

* NodeMCU board with ESP8266
* Two DS18B2 Temperature Sensors (More than one connected, you can simplify the code to connect just one)
* Available WiFi Signal with known user credentials

## Installation

* First you have to flash micropython firmware to your ESP8266 board with esptool.py if you did not before. (to download the firmware go to https://micropython.org/download/?port=esp8266)
* Clone the project (git clone https://github.com/omur-dalan/micropython-ESP8266-DS18B20.git)
* Use any ide or cli to upload project files to the board (https://code.visualstudio.com, https://marketplace.visualstudio.com/items?itemName=pycom.Pymakr)

## Features

* Board will adverstise a JSON data from its ip address

## Extra (Monitoring)

* You can use any monitoring application (https://www.zabbix.com etc.) to monitor trends or trigger alarms.
* Use HTPP Agent method and JSON preproccessing like "$.sensors[0].temperature" and "$.sensors[1].temperature" to get seperate sensor values.
