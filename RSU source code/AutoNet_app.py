# -*- coding: utf-8 -*-

import wifimodule
import socket
import time
import sys
import random

HOST = '169.254.200.13'
PORT =  5005
BUFFER_SIZE = 8
count = 0

#traffic light variables
traf_resp = ''
prev_traf_resp = ''
next_traf_resp = ''

#setup message data
def chooseResponse(req_msg):
    # responses for traffic light state request
    global traf_resp
    global prev_traf_resp
    global next_traf_resp
    
    if req_msg == 'traffic':
        if (next_traf_resp == '') and (prev_traf_resp == ''):
            prev_traf_resp = 'red'
            next_traf_resp = 'yellow'

        if (next_traf_resp == 'yellow') and (prev_traf_resp == 'red'):
            prev_traf_resp = 'yellow'
            next_traf_resp = 'green'
            traf_resp = 'yellow'
            return traf_resp

        if (next_traf_resp == 'green') and (prev_traf_resp == 'yellow'):
            prev_traf_resp = 'green'
            next_traf_resp = 'yellow'
            traf_resp = 'green'
            return traf_resp

        if (next_traf_resp == 'yellow') and (prev_traf_resp == 'green'):
            prev_traf_resp = 'yellow'
            next_traf_resp = 'red'
            traf_resp = 'yellow'
            return traf_resp 

        if (next_traf_resp == 'red') and (prev_traf_resp == 'yellow'):
            prev_traf_resp = 'red'
            next_traf_resp = 'yellow'
            traf_resp = 'red'
            return traf_resp
            
    #response to other request goes here
    
#set up wifi reception
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(1)
except socket.error as errmsg:
        if s:
                s.close()
                print (errmsg)
                sys.exit(1)

def receiveOnWifi():
    conn, addr = s.accept()
    try:
            data = conn.recv(BUFFER_SIZE)
    finally:
            # for traffic information
            if data:
                resp_data = chooseResponse(data)
                try:
                    time.sleep(3) # delay between sending responses
                    conn.sendall(resp_data)
                finally:
                    conn.close()
                    return data
            else:
                conn.close()
                return 'No data received'
while 1:
    rx_data = receiveOnWifi()
    print 'Received message :'+ rx_data
    
    time.sleep(1)
