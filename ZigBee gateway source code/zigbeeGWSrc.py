#!/usr/bin/env python
 
import socket
import serial
import time
import sys

BUFFER_SIZE = 8 #18 #20  # Normally 1024, but fast response needed
s_data ='s_ready'
e_data = 'e_ready'

#set up Ethernet reception
HOST = '169.254.214.14'
PORT = 5005

try:
     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     s.bind((HOST, PORT))
     s.listen(1)
except socket.error as msg:
     if s:
        s.close()
        print msg
        sys.exit(1)

def receiveOnEthernet(s_data):
    conn, addr = s.accept()
    try:
        data = conn.recv(BUFFER_SIZE)
    finally:
        try:
            conn.sendall(s_data)
        finally:
            conn.close()
            return data

#set up of serial communication
com_port = "/dev/ttyUSB0"
ser = serial.Serial(com_port, 9600)

def receiveOnSerial():
     data = ser.readline()
     #data = ser.read(BUFFER_SIZE)
     return data

def sendOverSerial(data):
     ser.write(data)
     ser.write('\r')
     ser.write('\n')

while 1:
     s_data = receiveOnSerial()
     if not s_data:
          s_data ='s_ready'
          
     print "From Serial: " + s_data #temporal
     
     e_data = receiveOnEthernet(s_data)
     print "From Ethernet: " + e_data #temporal

     time.sleep(2)
    
     sendOverSerial(e_data)

     



