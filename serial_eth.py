#!/usr/bin/env python
 
import socket
import serial
import time
import sys

BUFFER_SIZE = 8 #18 #20  # Normally 1024, but we want fast response

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

def receiveOnEthernet():
     conn, addr = s.accept()
     try:
          data = conn.recv(BUFFER_SIZE)
     finally:
          conn.close()
          return data

#set up Ethernet transmission
def sendOverEthenet(data):
     TCP_IP = '169.254.190.76'
     TCP_PORT = 5010
     try:
          s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
          s.connect((TCP_IP, TCP_PORT))
     except socket.error as msg:
          if s:
		s.close()
                print msg
                sys.exit(1)
     s.send(data)
     s.close()

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
     e_data = receiveOnEthernet()
     
     if e_data:
          print "From Ethernet: " + e_data #temporal
          sendOverSerial(e_data)

     time.sleep(2)
     
     s_data = receiveOnSerial() 
     
     if s_data:
          print "From Serial: " + s_data #temporal
          sendOverEthenet(s_data)
     


