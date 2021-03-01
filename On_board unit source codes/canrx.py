#!/usr/bin/env python

#canrx.py

import can
import time

bus = can.interface.Bus(channel='can0', bustype='socketcan_native')

while 1:
    msg = bus.recv()
    if msg:
        print(msg)
#notifier = can.Notifier(bus, [can.Printer()])
