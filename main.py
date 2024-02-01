'''
This code reads the temperature and air pressure from a BMP280 sensor and then sends it to ThingSpeak where it gets put in a graph.
'''

import time
from bmp280 import BMP280
from smbus2 import SMBus
import requests

writeAPIKey = "V5RTSR8W97XL0NH4"  # Put the write API Key of the channel here

# Initialise the BMP280
bus = SMBus(1)
bmp280 = BMP280(i2c_dev=bus)

while True:
    # Get data from the BMP280
    temperature = bmp280.get_temperature()
    pressure = bmp280.get_pressure()
    print('{:0.2f}*C, {:0.2f}hPa'.format(temperature, pressure))
    data = '&field1={:0.2f}&field2={:0.2f}'.format(temperature, pressure)

    # Send data to ThingSpeak
    response = requests.post('https://api.thingspeak.com/update?api_key=' + writeAPIKey+data)
    if response:
        print('Data sent succesfully')
    else:
        print('Error occurred with response:',response)

    time.sleep(10)