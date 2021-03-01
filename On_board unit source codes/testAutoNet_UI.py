#!/usr/bin/python3
import tkinter as tk
import meter as m
import can
#import time

class Window(tk.Frame):
    def __init__(self, master,*args,**kwargs):
        super(Window,self).__init__(master,*args,**kwargs)

        #display the meters
        self.dialsPanel = tk.LabelFrame(self,text="Monitor Panel")
        self.dialsPanel.pack(fill="both", expand="yes")

        #Label for meter1
        self.mlabel1 = tk.Label(self.dialsPanel, text="SPEED")
        self.mlabel1.pack(side=tk.LEFT)

        #Label for meter2
        self.mlabel2 = tk.Label(self.dialsPanel, text="TEMPERATURE")
        self.mlabel2.pack(side=tk.RIGHT) 

        #speed meter
        self.meter1 = m.Meter(self.dialsPanel,height = 300,width = 300)
        self.meter1.setrange(20,90)
        self.meter1.pack(side=tk.LEFT)

        #temperature meter
        self.meter2 = m.Meter(self.dialsPanel,height = 300,width = 300)
        self.meter2.setrange(20,90)
        self.meter2.pack(side=tk.RIGHT)


        #display the controllers
        self.controlPanel = tk.LabelFrame(self,text="Control Panel")
        self.controlPanel.pack(fill="both", expand="yes")

        #variables for collecting set values
        self.var1 = tk.DoubleVar()
        self.var2 = tk.DoubleVar()

        #slider controls
        self.speedCtrl = tk.Scale(self.controlPanel,label="SPEED", fg="red", width = 15
                                  ,variable = self.var1
                                  ,from_ = 20, to = 90
                                  ,orient = tk.HORIZONTAL
                                  ,command = self.setSpeed)
        self.speedCtrl.pack(side=tk.LEFT)

        self.tempCtrl = tk.Scale(self.controlPanel,label="TEMPERATURE", fg="red", width = 15
                                  ,variable = self.var2
                                  ,from_ = 20, to = 90
                                  ,orient = tk.HORIZONTAL
                                  ,command = self.setTemp)
        self.tempCtrl.pack(side=tk.LEFT)

        #button for sending data on network
        self.tempBtn = tk.Button(self.controlPanel,text="SEND TEMPERATURE"
                                  , fg="red", command=self.sendTemp)
        self.tempBtn.pack(side=tk.RIGHT)
        
        self.speedBtn = tk.Button(self.controlPanel,text="SEND SPEED"
                                  , fg="red", command=self.sendSpeed)
        self.speedBtn.pack(side=tk.RIGHT)

        #labels - temporal
        self.label1 = tk.Label(self)
        self.label1.pack()

        self.label2 = tk.Label(self)
        self.label2.pack()

    #CAN Transmission setup
    bus = can.interface.Bus(channel='can0', bustype='socketcan_native')

    def setSpeed(self,value):
        value = int(value)
        self.meter1.set(value)

    def setTemp(self,value):
        value = int(value)
        self.meter2.set(value)

    def sendSpeed(self):
        speedData = str(self.var1.get())
        self.label1.config(text = "Speed is " + speedData + " km/s") #temporal
        msgData = str(int(self.var1.get())) 
        if msgData:
            msg = can.Message(arbitration_id=0x7de,data = msgData.encode('utf-8'))
            self.bus.send(msg)

    def sendTemp(self):
        tempData = str(self.var2.get())
        self.label2.config(text = "Temperature is " + tempData + " Degree Celsius")#temporal
        tmsgData = str(int(self.var2.get()))
        if tmsgData:
            msg = can.Message(arbitration_id=0x7df,data = tmsgData.encode('utf-8'))
            self.bus.send(msg)              

class App(tk.Tk):
    def __init__(self):
        super(App,self).__init__()
      
        self.title('Test Panel')
     
        Window(self).pack()
                 
App().mainloop()


#root = tk.Tk()
#interface code goes here

#run or display interface
#root.mainloop()
#root.destroy() #optional
