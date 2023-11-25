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

```cd /opt/templogger && sudo bash /opt/templogger/configure_templogger.sh ``` 

      Updating the system, installing the required system tools
       * python3
       * i2c-tools 
       * python3-pip 
       * libgpiod-dev
      
       Installing the Python libraries indicated in the requirements.txt using pip3
       
      Create the systemd service to run the script 

## Troubleshooting
A script called test.py has been added to the repository that can be run directly to query the sensor, print temperature and humidity data to the console, and send that data to the Adafruit feeds immediately. It can be run using the following command:
```sudo python3 /opt/templogger/test.py```

To check if the I2C sensor is properly detected use the command. Look for the I2C address, in the case of the SHT45 chip it's 44.
```i2cdetect -y 1
     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:                         -- -- -- -- -- -- -- --
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
40: -- -- -- -- 44 -- -- -- -- -- -- -- -- -- -- --
50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
70: -- -- -- -- -- -- -- --
```

You can verify I2C is enabled on your system by checking that the line is uncommented in your /boot/config.txt
Make sure there is no hashmark (#) at the start of the output.

```grep dtparam=i2c_arm=on /boot/config.txt```

To check to see if the reporting service is running use this command. The output will tell you if the service has run recently and what the exit code was if it is active. 
```
sudo service temperature-probe status

● temperature-probe.service - Reads data from SHT45 sensor and uploads to Adafruit IO
     Loaded: loaded (/etc/systemd/system/temperature-probe.service; enabled; vendor preset: enabled)
     Active: activating (auto-restart) since Thu 2023-10-19 22:59:21 PDT; 4min 43s ago
TriggeredBy: ● temperature-probe.timer
    Process: 751 ExecStart=/usr/bin/python3 /opt/templogger/temp_probe.py (code=exited, status=0/SUCCESS)
   Main PID: 751 (code=exited, status=0/SUCCESS)
        CPU: 1.698s

Oct 19 22:59:21 IO systemd[1]: temperature-probe.service: Consumed 1.698s CPU time.
```
