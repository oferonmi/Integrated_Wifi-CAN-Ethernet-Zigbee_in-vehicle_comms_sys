#/usr/bin/env python

from __future__ import print_function

import can
import socket

#setting up can interface
bus = can.interface.Bus(channel='can0', bustype='socketcan_native')

def sendOverCAN(d_payload):
        msg = can.Message(arbitration_id=0x7de,data = d_payload)
        bus.send(msg)

#setting up ethernet connection
HOST = '169.254.190.76'  #socket.gethostname()
PORT = 5010
BUFFER_SIZE = 8 #18 #1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

#conn, addr = s.accept()

def receiveOnEthernet():
        conn, addr = s.accept()
        data = conn.recv(BUFFER_SIZE)
        conn.close()
        return data

while 1:
        e_data = receiveOnEthernet()
        print (e_data) #temporal

        if e_data:
                sendOverCAN(e_data)
                
        
##bus = can.interface.Bus(channel='can0', bustype='socketcan_native')
##msg = can.Message(arbitration_id=0x7de,data=[0, 25, 0, 1, 3, 1, 4, 1])
##bus.send(msg)
