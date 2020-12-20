class HeaterWrapper(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(HeaterWrapper, cls).__new__(cls)
        return cls.instance

    def tie(self, heater):
        if not hasattr(self, 'heater'):
            self.heater = heater

    def get(self):
        return self.heater