# -*- coding: utf-8 -*-
#!/usr/bin/env python3

import wifimodule
import socket
import time
import sys
import can

msg_data = 'traffic' #to request traffic light status
BUFFER_SIZE = 8

#set up wifi transmission
def sendOverWifi(msg):
    IP = '169.254.200.13'
    PORT = 5005
    wi_msg = str(msg).encode('utf-8')
    
    try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((IP, PORT))
    except socket.error as errmsg:
            if s:
                    s.close()
                    print (errmsg)
                    sys.exit(1)

    s.sendall(wi_msg)
    try:
        r_resp = s.recv(BUFFER_SIZE)
    finally:
        s.close()
    return r_resp


#CAN transmission setup
bus = can.interface.Bus(channel='can0', bustype='socketcan_native')

def sendOverCAN(frame_data):
    wi_msg = can.Message(arbitration_id=0x8df,data = frame_data)
    bus.send(wi_msg)

while 1:
    rx_data = sendOverWifi(msg_data)
    #msg_data += 1

    if rx_data:
        print ('Received response :'+ str(rx_data))
        sendOverCAN(rx_data)
    
    time.sleep(1)
                
