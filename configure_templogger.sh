#!/bin/bash

# Very basic (and untested) script to configure the system for 
#

echo "Updating the system prior to installling required dependancies."
echo "This can take some time." 

apt-get update
echo "APT-GET Update completed!"

apt-get upgrade
echo "System update completed!"

apt-get install -y i2c-tools python3 python3-pip libgpiod-dev 
echo "System packages installed!"

pip3 install -r requirements.txt
echo "Python libraries installed!"

echo " "
echo " "

cp /opt/templogger/temperature-probe.service /etc/systemd/system/.
cp /opt/templogger/temperature-probe.timer /etc/systemd/system/.

systemctl daemon-reload
systemctl start temperature-probe.service
