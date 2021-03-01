# -*- coding: utf-8 -*-

import wifimodule
import socket
import time
import sys
import threading

HOST = '169.254.200.13'
PORT =  5005
BUFFER_SIZE = 8
count = 0

#set ip wifi reception
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
            if data:
                #return data
                try:
                    conn.sendall(data)
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


##ssid = 'RPi_net'
##password = 'raspberry'
###connect to saved network with SSID 'Pi_net'
##
##wifi_conn = wifimodule.Connect(ssid, password)
##
##if wifi_conn == False:
##    print 'wifi connection to ' + ssid + ' failed.'
##else:
##    print 'wifi connected to '+ ssid + '.' #temporal
##
##if wifi_conn.ssid == 'RPi_net'
##    IP = wifi_conn.address
##    PORT =  5005
##    BUFFER_SIZE = 8
##    
##    #set ip wifi reception
##    try:
##        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
##        s.bind((HOST, PORT))
##        s.listen(1)
##    except socket.error as errmsg:
##            if s:
##                    s.close()
##                    print (errmsg)
##                    sys.exit(1)
##
##    def receiveOnWifi():
##        conn, addr = s.accept()
##        try:
##                data = conn.recv(BUFFER_SIZE)
##        finally:
##                conn.close()
##                return data
##
##    #set up wifi transmission
##    def sendOverWifi(msg):
##        HOST = '169.254.214.14'
##        PORT = 5005
##
##        try:
##                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
##                s.connect((HOST, PORT))
##        except socket.error as errmsg:
##                if s:
##                        s.close()
##                        print (errmsg)
##                        sys.exit(1)
##
##        s.send(msg)
##        s.close()
##
##    while 1:
##        rx_data = receiveOnWifi()
##        print 'Received message :'+ rx_data
##
##        time.sleep(1)
##
##        sendOverWifi('Bonjour')
##        
##from wifi import Cell, Scheme
##
###connect to a network
##wnet_scheme = Scheme.find('wlan0', 'pi_net')
##
##if wnet_scheme == None:
##    #search for network
##    wnet = Cell.all('wlan0')[0]
##    wnet_scheme = Scheme.for_cell('wlan0', 'pi_net', wnet, passkey)
##    wnet_scheme.save()
##    wnet_scheme.activate()
##else:
##    wnet_scheme.activate()
