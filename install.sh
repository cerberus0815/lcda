#!/bin/bash
if [ "$(id -u)" != "0" ]; then
	echo "Please re-run as sudo."
	exit 1
fi

echo "Automatisierter Installer fuer I2C LCD-Displays"
echo "Programm geschrieben von IT&Web Schwendenwein"
echo "Update von APT & Installiert python-smbus, falls Passwort angefordert wird, bitte eingeben!"
apt-get update
apt-get install python-smbus -y
echo "Sollte nun installiert sein, checke System-Revision"
revision=`python -c "import RPi.GPIO as GPIO; print GPIO.RPI_REVISION"`

if [ $revision = "1" ]
then
echo "I2C Pins gefunden auf 0"
cp installConfigs/i2c_lib_0.py ./i2c_lib.py
else
echo "I2C Pins gefunden auf 1"
cp installConfigs/i2c_lib_1.py ./i2c_lib.py
fi
echo "I2C Library für RaspberryPi, wenn Ihr die Revision aendern wollt ist eine aenderung in der i2c_lib.py notwendig!"
echo "Bearbeite nun modules & blacklist. Schaltet die I2C-Pins frei"
cp installConfigs/modules /etc/
cp installConfigs/raspi-blacklist.conf /etc/modprobe.d/
printf "dtparam=i2c_arm=1\n" >> /boot/config.txt


echo "Alles Erledigt. Bitte eine Taste druecken fuer Reboot, nach Reboot fuehre diesen Befehl aus:"
echo "'sudo python lcd.py' vom lcd Verzeichnis"
read -n1 -s
sudo reboot
