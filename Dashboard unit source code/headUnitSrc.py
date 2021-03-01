#!/usr/bin/env python3      

import can
import socket
import time
import sys

#incoming_data = 'ready'
can_data = 'c_ready'
e_data = 'e_ready'

BUFFER_SIZE = 8 #18 #1024

#set up Ethernet connection
def sendOverEthernet(e_msg):
        HOST = '169.254.214.14'
        PORT = 5005

        try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((HOST, PORT))
        except socket.error as errmsg:
                if s:
                        s.close()
                        print (errmsg)
                        sys.exit(1)

        s.sendall(e_msg)
        
        try:
                incoming_data = s.recv(BUFFER_SIZE)
        finally:
                s.close()
                return incoming_data
    
#set up CAN interface
bus = can.interface.Bus(channel='can0', bustype='socketcan_native')

def receiveOnCAN():
        msg = bus.recv()
        return msg.data

def sendOverCAN(d_payload):
        msg = can.Message(arbitration_id=0x8de,data = d_payload)
        bus.send(msg)

while 1:
        can_data = receiveOnCAN()
        print ("From CAN bus: " + can_data.decode('utf-8')) #temporal
        
        e_data = sendOverEthernet(can_data)

        sendOverCAN(e_data)
        print ("From Ethernet: " + str(e_data)) #temporal
        
        time.sleep(2)         
        


