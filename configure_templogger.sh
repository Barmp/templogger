#!/bin/bash

# Very basic (and untested) script to configure the system for 
#

echo "Making sure I2C is enabled on system"
sed -i -r 's/#dtparam=i2c_arm=on/dtparam=i2c_arm=on/' /boot/config.txt
echo "Complete"
echo ""

echo "Updating the system prior to installling required dependancies."
echo "This can take some time."
echo ""
echo "..."

apt-get update -u -q
echo "APT-GET Update completed!"
echo ""
echo "..."

apt-get upgrade -u -q
echo "System update completed!"
echo ""
echo "..."

apt-get install -u -q i2c-tools python3 python3-pip libgpiod-dev
echo "System packages installed!"
echo ""
echo "..."

pip3 install -r requirements.txt -U
echo "Python libraries installed!"
echo ""
echo "..."

echo "Testing the sensor and sending data to Adafruit feeds."
python3 /opt/templogger/test.py
echo ""
echo "Test complete!"
echo "..."

echo "Installing as a system service"
cp /opt/templogger/temperature-probe.service /etc/systemd/system/.
cp /opt/templogger/temperature-probe.timer /etc/systemd/system/.

systemctl daemon-reload
systemctl enable temperature-probe
service temperature-probe start
echo ""
echo "Service installed."
echo ""
echo "Please restart the system to complete the installation. \
If data is not being sent to your Adafruit IO Feed within a few minutes \ 
of starting back up you can use "sudo service temperature-probe status" to \ 
check on the state of the service and it's last run / completion time if any."

