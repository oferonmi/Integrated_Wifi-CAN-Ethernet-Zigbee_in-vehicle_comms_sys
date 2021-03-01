#!/usr/bin/env python
 
import socket
import time
import serial

#Setup Ethernet communication

def sendOverEthenet(data):
        TCP_IP = '169.254.190.76'
        TCP_PORT = 5010
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((TCP_IP, TCP_PORT))
        s.send(data)
        #s.send('\n')
        #s.send('\r')
        #time.sleep(2)
        s.close()

#setup serial communication
com_port = "/dev/ttyUSB0"
ser = serial.Serial(com_port, 9600)
BUFFER_SIZE = 8 #18 #1024

def receiveOnSerial():
     data = ser.read(BUFFER_SIZE)
     return data

while 1:
        s_data = receiveOnSerial()
        print s_data #temporal
        
        if s_data:
                sendOverEthenet(s_data)
