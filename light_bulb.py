from ABCs import *

class LightBulb(Component, Switchable):
    def __init__(self, id, is_on):
        super().__init__()
        self.type = 'light_bulb'
        self.id = id
        self.is_on = is_on
        
    def info(self):
        print("[Component]:")
        print("\t id:" + self.id)
        print("\t type:" + self.type)
        print("\t is_on:" + str(self.is_on))
    
    def turnOn(self):
        self.is_on = 1
        SocketWrapper().emmit_update_var(self.id, "is_on", self.is_on)
        
    def turnOff(self):
        self.is_on = 0
        SocketWrapper().emmit_update_var(self.id, "is_on", self.is_on)
        
    def update_value(self, var_name, var):
        if var_name == 'is_on':
            if var == 1:
                self.turnOn()
            elif var == 0:
                self.turnOff()
        
            