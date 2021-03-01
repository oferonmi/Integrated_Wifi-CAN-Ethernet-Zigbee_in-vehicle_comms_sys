#!/usr/bin/env python3

#cantx.py

import can
import time
import random as rnd

bus = can.interface.Bus(channel='can0', bustype='socketcan_native')
while 1:
        # simulating speed change
        sdata = rnd.randint(20, 90)
        cdata = str(sdata).encode('utf-8')
        msg_i = can.Message(arbitration_id=0x7de,data = cdata)
        bus.send(msg_i)

        time.sleep(2)

        #simulating temperature change
        tdata = rnd.randint(20, 40)
        cdata = str(tdata).encode('utf-8') 
        msg_ii = can.Message(arbitration_id=0x7df,data = cdata)
        bus.send(msg_ii)

        time.sleep(2)
        
