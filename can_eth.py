#!/usr/bin/env python      

import can
import socket
import time
import sys

#set up Ethernet reception
HOST = '169.254.190.76'
PORT = 5010
BUFFER_SIZE = 8 #18 #1024

try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((HOST, PORT))
        s.listen(1)
except socket.error as errmsg:
        if s:
                s.close()
                print (errmsg)
                sys.exit(1)

def receiveOnEthernet():
        conn, addr = s.accept()
        try:
                data = conn.recv(BUFFER_SIZE)
        finally:
                conn.close()
                return data

#set up Ethernet transmission
def sendOverEthernet(msg):
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

        s.send(msg)
        s.close()

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

        if can_data:
                print ("From CAN bus: " + can_data.decode('utf-8')) #temporal
                sendOverEthernet(can_data)

        time.sleep(2)
        
        e_data = receiveOnEthernet()
        
        if e_data:
                if type(e_data) != str:
                        e_data = str(e_data)
                        print ("From Ethernet: " + e_data) #temporal
                else:
                        print ("From Ethernet: " + e_data.decode('utf-8')) #temporal
                        sendOverCAN(e_data)

        time.sleep(2)         
        


