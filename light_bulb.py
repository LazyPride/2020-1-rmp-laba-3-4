from ABCs import *

class LightBulb(Component, Switchable):
    def __init__(self, is_on):
        super().__init__()
        self.type = 'light_bulb'
        self.is_on = is_on
        
    def info(self):
        print("[Component]:")
        print("\t type:" + self.type)
        print("\t is_on:" + str(self.is_on))
