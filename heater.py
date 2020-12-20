import threading
from SocketWrapper import SocketWrapper
from ABCs import *

class Heater(Component, Switchable, Adjustable, Bounded):
    def __init__(self, id, is_on, min, max, now):
        super().__init__()
        self.type = 'Heater'
        self.id = id
        self.is_on = is_on
        self.min = min
        self.max = max
        self.now = now
        
    def info(self):
        print("[Component]:")
        print("\t id:" + self.id)
        print("\t type:" + self.type)
        print("\t is_on:" + str(self.is_on))
        print("\t min:" + str(self.min))
        print("\t max:" + str(self.max))
        print("\t now:" + str(self.now))
    
    def start(self, updateTime):
        threading.Timer(updateTime, self.start, [updateTime],{} ).start()
        if self.is_on == 1:
            self.now += 1
            if int(self.now) >= int(self.max):
                self.turnOff()
        else:
            self.now -= 1
            if int(self.now) <= int(self.min):
                self.turnOn()
        SocketWrapper().emmit_update_var(self.id, "now", self.now)

    def turnOn(self):
        self.is_on = 1
        SocketWrapper().emmit_update_var(self.id, "is_on", self.is_on)
        
    def turnOff(self):
        self.is_on = 0
        SocketWrapper().emmit_update_var(self.id, "is_on", self.is_on)
        
    def setMin(self, min):
        self.min = min
        SocketWrapper().emmit_update_var(self.id, "min", self.min)

    def setMax(self, max):
        self.max = max
        SocketWrapper().emmit_update_var(self.id, "max", self.max)
        
    def update_value(self, var_name, var):
        if var_name == 'is_on':
            if var == 1:
                self.turnOn()
            elif var == 0:
                self.turnOff()
        elif var_name == 'min':
            self.setMin(var)
        elif var_name == 'max':
            self.setMax(var)
            