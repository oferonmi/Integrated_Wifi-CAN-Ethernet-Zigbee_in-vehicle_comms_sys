#!/usr/bin/env python
 
import socket
import serial
import time

BUFFER_SIZE = 18 #20  # Normally 1024, but we want fast response

#set up serial communication
com_port = "/dev/ttyUSB0"
ser = serial.Serial(com_port, 9600)

def sendOverSerial(data):
     ser.write(data)
     ser.write('\n')
     ser.write('\r')

#set up Ethernet communication
#TCP_IP = '127.0.0.1'
TCP_IP = '169.254.214.14'
TCP_PORT = 5005
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)
 
#conn, addr = s.accept()

def receiveOnEthernet():
     conn, addr = s.accept()
     data = conn.recv(BUFFER_SIZE)
     conn.close()
     return data

#print 'Connection address:', addr

while 1:
     e_data = receiveOnEthernet()
     print e_data #temporal
     
     #send ethernet data over only free serial interface
     if e_data:
          sendOverSerial(e_data)

     
#conn.close()
