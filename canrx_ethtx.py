#!/usr/bin/env python      

import can
import socket
import time

#bus = can.interface.Bus(channel='can0', bustype='socketcan_native')

def receiveOnCAN():
        bus = can.interface.Bus(channel='can0', bustype='socketcan_native')
        msg = bus.recv()
        return msg.data

#HOST = '169.254.214.14'  #socket.gethostname()
#PORT = 5005

#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#s.connect((HOST, PORT))

def sendOverEthernet(msg):
        HOST = '169.254.214.14'  #socket.gethostname()
        PORT = 5005
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        s.connect((HOST, PORT))
        s.send(msg)
        time.sleep(4)
        #s.send('\n')
        #s.send('\r')
        s.close()

while 1:
        can_data = receiveOnCAN()
        print(can_data) #temporal
                   
        if can_data:
                sendOverEthernet(can_data)
                

