#!/usr/bin/env python3

# Created by Barmp - October 2023
# Based on code and documentation created by Adafruit.
# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import board
import adafruit_sht4x
#from Adafruit_IO import Client, Feed
import Adafruit_IO as AdafruitIO
import configparser
import time

# Read the configuration information for connecting to Adafruit IO 
config = configparser.ConfigParser()
config.read('adafruitio.conf')
adafruit_key = config['Adafruit']['ADAFRUIT_IO_KEY'].strip('"')
adafruit_username = config['Adafruit']['ADAFRUIT_IO_USERNAME'].strip('"')
temperature_feed = config['Adafruit']['TEMP_FEED'].strip('"')
relhumidity_feed = config['Adafruit']['HUMID_FEED'].strip('"')
errors_feed = config['Adafruit']['ERRORS_FEED'].strip('"')

# Create an instance of the REST client.
aio = AdafruitIO.Client(adafruit_username, adafruit_key)
# Create sensor object, using the board's default I2C bus.
i2c = board.I2C()  # uses board.SCL and board.SDA
# Create an instance of the sensor that we can poll for 
SHT45 = adafruit_sht4x.SHT4x(i2c)

for i in range(59):
    # Send humidity and temperature feeds to Adafruit IO
    try:
        aio.send(temperature_feed, str(SHT45.temperature))
        aio.send(relhumidity_feed, str(SHT45.relative_humidity))
    
    except AdafruitIO.RequestError as err:
        pass
    except AdafruitIO.ThrottlingError as err: 
        pass

        
        #aio.send(errors_feed, str(err))

    time.sleep(60)
###
# Available API calls for the SHT45 sensor
#SHT45.temperature
#SHT45.relative_humidity
#SHT45.measurements
#SHT45.mode
#SHT45.serial_number
#SHT4x.reset()
###
