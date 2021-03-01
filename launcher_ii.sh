#!/bin/bash
#launcher.sh

# navigating to working directory and execution of scripts
#sleep 30s

cd /home/pi/hardbyte-python-can-4085cffd2519
sudo python3 testAutoNet_dash.py

#script to keep terminal open
exec $SHELL
