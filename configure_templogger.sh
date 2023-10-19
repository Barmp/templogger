#!/bin/bash

# Very basic (and untested) script to configure the system for 
#

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
echo "installing as a system service"
cp /opt/templogger/temperature-probe.service /etc/systemd/system/.
cp /opt/templogger/temperature-probe.timer /etc/systemd/system/.

systemctl daemon-reload
systemctl start temperature-probe.service
echo ""
echo "Completed!"
