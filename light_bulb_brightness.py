from ABCs import *

class LightBulbBrightness(Component, Switchable, Adjustable, Bounded):
    def __init__(self, id, is_on, now):
        super().__init__()
        self.type = 'light_bulb_brightness'
        self.id = id
        self.is_on = is_on
        self.min = 0
        self.max = 100
        self.now = now
        
    def info(self):
        print("[Component]:")
        print("\t id:" + self.id)
        print("\t type:" + self.type)
        print("\t is_on:" + str(self.is_on))
        print("\t min:" + str(self.min))
        print("\t max:" + str(self.max))
        print("\t now:" + str(self.now))
    