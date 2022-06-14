#!/bin/bash

#update the system
echo "Your! system is updating!..."
sudo apt update -y
#upgrade the system
echo "Your! system is upgrading!..."
sudo apt upgrade -y
#install python
echo "Installing python latest version!..."
sudo apt install python3 -y 
#check python version
echo "Checking Python3 Version!..."
python3 -V
#install Django
echo "Installing Django!..."
sudo apt install python3-django
#check Django version
echo "Checking Django Version!..."
django-admin --version
echo "Django are Successfully installed!."
