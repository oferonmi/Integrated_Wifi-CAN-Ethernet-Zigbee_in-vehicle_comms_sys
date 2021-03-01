#!/usr/bin/python3
import tkinter as tk
import tkinter.font as tkf
import can
#import time

class Window(tk.Frame):
    def __init__(self, master,*args,**kwargs):
        super(Window,self).__init__(master,*args,**kwargs)

        #display area
        #variable containers
        self.cmsg1 = tk.StringVar()
        self.cmsg1.set('0')
        self.cmsg2 = tk.StringVar()
        self.cmsg2.set('0')
        self.cmsg3 = tk.StringVar()
        self.cmsg3.set('0')
        self.cmsg4 = tk.StringVar()
        self.cmsg4.set('0')
        
        self.dash = tk.LabelFrame(self,text="Notification Panel")
        self.dash.pack(fill="both", expand="yes")
        
        self.speedNtf = tk.LabelFrame(self.dash,text="SPEED")
        self.speedNtf.pack(fill="both", expand="yes", side=tk.LEFT)

        self.nlabel1 = tk.Label(self.speedNtf, font=("Helvetica", 80)
                                , fg = "red",textvariable = self.cmsg1 )
        self.nlabel1.pack()

        self.tempNtf = tk.LabelFrame(self.dash,text="TEMPERATURE")
        self.tempNtf.pack(fill="both", expand="yes", side=tk.LEFT )

        self.nlabel2 = tk.Label(self.tempNtf, font=("Helvetica", 80)
                                , fg = "red", textvariable = self.cmsg2)
        self.nlabel2.pack()
        
        self.xNtf = tk.LabelFrame(self.dash,text="EXTERNAL")
        self.xNtf.pack(fill="both", expand="yes", side=tk.LEFT)

        self.nlabel3 = tk.Label(self.xNtf, font=("Helvetica", 80)
                                , fg = "red", textvariable = self.cmsg3)
        self.nlabel3.pack()

        self.inNtf = tk.LabelFrame(self.dash,text="OTHER INTERNAL")
        self.inNtf.pack(fill="both", expand="yes", side=tk.LEFT)

        self.nlabel4 = tk.Label(self.inNtf, font=("Helvetica", 80)
                                , fg = "red", textvariable = self.cmsg4)
        self.nlabel4.pack()

        #receive button area
        self.ctrlArea = tk.LabelFrame(self.dash,text="Control")
        self.ctrlArea.pack(fill="both", expand="yes")

        self.ctrlBtn = tk.Button(self.ctrlArea,text="START"
                                  , fg="red", command=self.canNotify)
        self.ctrlBtn.pack()
        
        #CAN Transmission setup
        self.bus = can.interface.Bus(channel='can0', bustype='socketcan_native')
        #self.msg = self.bus.recv().data.decode('utf-8')
        #self.cmsg1.set(self.msg)
        
    def canNotify(self):
        #bus = can.interface.Bus(channel='can0', bustype='socketcan_native')
        msg = self.bus.recv()
        if msg.arbitration_id==0x7de:
            cdata = msg.data.decode('utf-8')
            self.cmsg1.set(cdata)

        if msg.arbitration_id==0x7df:
            cdata = msg.data.decode('utf-8')
            self.cmsg2.set(cdata)
        #self.nlabel1.config(text = self.cmsg1)
        self.after(1000, self.canNotify)
        
class App(tk.Tk):
    def __init__(self):
        super(App,self).__init__()
      
        self.title('Display Panel')
     
        Window(self).pack()
                 
App().mainloop()
