# templogger
Simple python project to send data from a SHT45 sensor to Adafruit IO as a systemd service

## Setup
This guide assumes you've installed Raspberry Pi OS and created an initial user for adminstrative purposes.

1. Use raspi-config to enable the following two features under "Interface Options"
  * SSH - Enabled
  * I2C - Enabled

2. Clone this git repo into the systems /opt diretory: 

```sudo git clone https://github.com/Barmp/templogger.git /opt/templogger```

3. Modify the /opt/templogger/adafruitio.conf file with your Adafruit credentials and feed names for the temperature and humidity data

```sudo nano /opt/templogger/adafruitio.conf```

4. Run the configuration script, which completes the steps listed below: 

```sudo bash /opt/templogger/configure_templogger.sh ``` 

      Updating the system, installing the required system tools
       * python3
       * i2c-tools 
       * python3-pip 
       * libgpiod-dev
      
       Installing the Python libraries indicated in the requirements.txt using pip3
       
      Create the systemd service to run the script 
