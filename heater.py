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
            if int(self.now) >= int(self.max):
                self.turnOff()
            else:
                if int(self.now) < 100:
                    self.now = self.now + 1
        else:
            if self.now > 0:
                self.now = self.now - 1
        self.__emmit__("temperature", self.now)

    def turnOn(self):
        self.is_on = 1
        print("The heater in {} is On({}) to {} degrees".format(self.roomName, self.is_on, self.max))
        self.__emmit__("isHeatingOn", self.is_on)
        
    def turnOff(self):
        self.is_on = 0
        print("The heater in {} is Off({})".format(self.roomName, self.is_on))
        self.__emmit__("isHeatingOn", self.is_on)
        
    def setMin(self, min):
        self.min = min
        self.__emmit__("min", self.min)

    def setMax(self, max):
        self.max = max
        self.__emmit__("max", self.max)
        
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
            
    def __emmit__(self, varName, varValue):
        msg = {}
        msg["roomName"] = self.roomName
        msg["varName"] = varName
        msg["varValue"] = varValue
        json_msg = json.dumps(msg)
        SocketWrapper().update(json_msg)