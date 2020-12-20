from abc import ABC, abstractmethod

class Component(ABC):
    def __init__(self):
        self.type = 'component'
        super().__init__()
        #print("FROM Component: type:" + self.type)
        
    def update_value(self, var_name, var):
        pass
        
    def setType(self, value):
        self.type = value
        
    def getType(self):
        return self.type
        
    def info(self):
        pass

class Adjustable(ABC):
    @abstractmethod
    def __init__(self):
        self.now = 0
        super().__init__()
        #print("FROM Adjustable: now:" + str(self.now))
        
    def adjust(self, value):
        self.now = value
        
    def getValue(self):
        return self.now

class Bounded(ABC):
    @abstractmethod
    def __init__(self):
        self.min = 0
        self.max = 0
        super().__init__()
        #print("FROM Bounded: min:" + str(self.min))
        #print("FROM Bounded: max:" + str(self.max))
        
     
    def setMin(self, min):
        self.min = min

    def setMax(self, max):
        self.max = max
        
    def getMin(self):
        return self.min
        
    def getMax(self):
        return self.max
        

class Switchable(ABC):
    @abstractmethod
    def __init__(self):
        self.is_on = 0
        super().__init__()
        #print("FROM Switchable: is_on:" + str(self.is_on))
        
        
    def turnOn(self):
        self.is_on = 1
        
    def turnOff(self):
        self.is_on = 0   
    
    def isOn(self):
        return self.is_on
