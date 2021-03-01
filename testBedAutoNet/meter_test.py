#https://www.raspberrypi.org/forums/viewtopic.php?f=91&t=106349&p=733365#p733365
import tkinter as tk
import meter as m

class Mainframe(tk.Frame):
    
   def __init__(self,master,*args,**kwargs):
      super(Mainframe,self).__init__(master,*args,**kwargs)
  
      self.meter = m.Meter(self,height = 300,width = 300)
      self.meter.setrange(20,90)
      self.meter.pack()
      
      tk.Scale(self,width = 15 ,from_ = 20, to = 90
      ,orient = tk.HORIZONTAL
      ,command = self.setmeter).pack()
      
      tk.Button(self,text = 'Quit',width = 15,command = master.destroy).pack()
      
   def setmeter(self,value):
      value = int(value)
      self.meter.set(value)
 
class App(tk.Tk):
    def __init__(self):
        super(App,self).__init__()
      
        self.title('Try Meter')
     
        Mainframe(self).pack()
                 
App().mainloop()
