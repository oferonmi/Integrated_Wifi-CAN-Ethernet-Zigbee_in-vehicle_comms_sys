#!/usr/bin/python3
import tkinter as tk
import tkinter.font as tkf
import meter as m
import can
#from can_eth import receiveOnEthernet 

class Window(tk.Frame):
    def __init__(self, master,*args,**kwargs):
        super(Window,self).__init__(master,*args,**kwargs)

        #display area
        #variable containers
        #self.cmsg1 = tk.StringVar()
        #self.cmsg1.set('0')
        #self.cmsg2 = tk.StringVar()
        #self.cmsg2.set('0')
        self.cmsg3 = tk.StringVar()
        self.cmsg3.set('0')
        #self.cmsg4 = tk.StringVar()
        #self.cmsg4.set('')
        
        self.dash = tk.LabelFrame(self,text="Notification Panel")
        self.dash.pack(fill="both", expand="yes")

        #speed notification
        self.speedNtf = tk.LabelFrame(self.dash,text="SPEED (km/h)")
        self.speedNtf.pack(fill="both", expand="yes", side=tk.LEFT)

        #speed meter
        self.meter1 = m.Meter(self.speedNtf,height = 300,width = 300)
        self.meter1.setrange(20,90)
        self.meter1.pack()

        #speed label nofication
        #self.nlabel1 = tk.Label(self.speedNtf, font=("Helvetica", 80)
                                #, fg = "red",textvariable = self.cmsg1 )
        #self.nlabel1.pack()

        #temperature notification
        self.tempNtf = tk.LabelFrame(self.dash,text="TEMPERATURE (Degree Celsius)")
        self.tempNtf.pack(fill="both", expand="yes", side=tk.LEFT)

        #temperature meter
        self.meter2 = m.Meter(self.tempNtf,height = 300,width = 300)
        self.meter2.setrange(20,90)
        self.meter2.pack()

        #temperature label notification
        #self.nlabel2 = tk.Label(self.tempNtf, font=("Helvetica", 80)
                                #, fg = "red", textvariable = self.cmsg2)
        #self.nlabel2.pack()
        
        self.inNtf = tk.LabelFrame(self.dash,text="OTHER INTERNAL DATA")
        self.inNtf.pack(fill="both", expand="yes",side=tk.BOTTOM )

        self.nlabel3 = tk.Label(self.inNtf, font=("Helvetica", 40)
                                , fg = "red", textvariable = self.cmsg3)
        self.nlabel3.pack(anchor=tk.CENTER)

        #notification from external eviron e.g traffic light
        self.xNtf = tk.LabelFrame(self.dash,text="TRAFFIC")
        self.xNtf.pack(fill="both", expand="yes",side=tk.BOTTOM )

        self.traf_indicator = tk.Canvas(self.xNtf, width =100, height = 150)
        self.traf_indicator.pack(anchor=tk.CENTER)
        
        self.circle_ind = self.traf_indicator.create_oval(10, 50, 85,125
                                                          , fill='red')
        #traffic notification label
        #self.nlabel4 = tk.Label(self.xNtf, font=("Helvetica", 80)
                                #, fg = "red", textvariable = self.cmsg4)
        #self.nlabel4.pack()

        #button area to initiate data reception
        self.ctrlArea = tk.LabelFrame(self.dash,text="Control")
        self.ctrlArea.pack(fill="both", expand="yes", side=tk.BOTTOM)

        self.ctrlBtn = tk.Button(self.ctrlArea,text="START"
                                  , fg="red", command=self.canNotify)
        self.ctrlBtn.pack(anchor=tk.CENTER)
        
        #CAN Transmission setup
        self.bus = can.interface.Bus(channel='can0', bustype='socketcan_native')

    def setSpeed(self,value):
        value = int(value)
        self.meter1.set(value)

    def setTemp(self,value):
        value = int(value)
        self.meter2.set(value)
       
    def canNotify(self):
        msg = self.bus.recv()
        if msg.arbitration_id==0x7de:
            cdata = msg.data.decode('utf-8')
            #self.cmsg1.set(cdata)
            self.setSpeed(cdata)

        if msg.arbitration_id==0x7df:
            cdata = msg.data.decode('utf-8')
            #self.cmsg2.set(cdata)
            self.setTemp(cdata) 
            
        if msg.arbitration_id==0x8de:
            cdata = msg.data.decode('utf-8')
            self.cmsg3.set(cdata)
            
        if msg.arbitration_id==0x8df:
            cdata = msg.data.decode('utf-8')
            #self.cmsg4.set(cdata)
            self.traf_indicator.itemconfig(self.circle_ind, fill=cdata
                                           , outline=cdata)
            
        self.after(1000, self.canNotify)
        
class App(tk.Tk):
    def __init__(self):
        super(App,self).__init__()
      
        self.title('Display Panel')
     
        Window(self).pack()
        
App().mainloop()
