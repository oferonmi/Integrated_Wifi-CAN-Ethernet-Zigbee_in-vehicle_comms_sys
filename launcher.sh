#!/bin/bash
#launcher.sh

sleep 20s

cd /home/pi/hardbyte-python-can-4085cffd2519
sudo python3 can_eth.py

#script to keep terminal open
exec $SHELL

