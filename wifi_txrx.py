# -*- coding: utf-8 -*-

import wifimodule
import socket
import time
import sys
import threading
import wifi

msg_data = 0
BUFFER_SIZE = 16
#ssid = 'RPi_net'
#password = 'raspberry'
#connect to saved network with SSID 'RPi_net'

#try:
#wifi_conn = wifimodule.Connect(ssid, password)
#except wifi.exceptions.ConnectionError as wifi_error:
    #print wifi_error
    #sys.exit(1)

#if wifi_conn == False:
    #print 'wifi connection to ' + ssid + ' failed.'
#else:
##    #print 'wifi connected to '+ ssid + '.' #temporal

#set up wifi transmission
def sendOverWifi(msg):
    IP = '169.254.200.13'
    PORT = 5005

    try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((IP, PORT))
    except socket.error as errmsg:
            if s:
                    s.close()
                    print (errmsg)
                    sys.exit(1)

    s.sendall(msg)
    try:
        r_resp = s.recv (BUFFER_SIZE)
    finally:
        s.close()
    return r_resp

while 1:
    #sendOverWifi('Bonjour')
    rx_data = sendOverWifi(str(msg_data))
    msg_data += 1

    if rx_data:
        print 'Received response :'+ rx_data 
    
    time.sleep(1)
                
