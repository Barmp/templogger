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

# Create an instance of the REST client.
aio = AdafruitIO.Client(adafruit_username, adafruit_key)
# Create sensor object, using the board's default I2C bus.
i2c = board.I2C()  # uses board.SCL and board.SDA
# Create an instance of the sensor that we can poll for 
SHT45 = adafruit_sht4x.SHT4x(i2c)

# Write temp and humidity data to console
print("Temp: " + str(SHT45.temperature))
print("Humidity: " + str(SHT45.relative_humidity))

# Send humidity and temperature feeds to Adafruit IO
aio.send(temperature_feed, str(SHT45.temperature))
aio.send(relhumidity_feed, str(SHT45.relative_humidity))
