import threading
from SocketWrapper import SocketWrapper

class Heater:
    def __init__(self, roomName, isHeatingOn, curTemp, maxTemp):
        self.roomName = roomName
        self.curTemp = curTemp
        self.maxTemp = maxTemp
        self.isOn = isHeatingOn
    
    def start(self, updateTime):
        threading.Timer(updateTime, self.start, [updateTime],{} ).start()
            if self.isOn == 1:
                if int(self.curTemp) >= int(self.maxTemp):
                    self.turnOff()
                else:
                    if int(self.curTemp) < 100:
                        self.curTemp = self.curTemp + 1
            else:
                if self.curTemp > 0:
                    self.curTemp = self.curTemp - 1
            self.__emmit__("temperature", self.curTemp)

    def turnOn(self):
        self.isOn = 1
        print("The heater in {} is On({}) to {} degrees".format(self.roomName, self.isOn, self.maxTemp))
        self.__emmit__("isHeatingOn", self.isOn)
        
    def turnOff(self):
        self.isOn = 0
        print("The heater in {} is Off({})".format(self.roomName, self.isOn))
        self.__emmit__("isHeatingOn", self.isOn)
        
    def update(self, jsonFile):
        if jsonFile["roomName"] == self.roomName:
            if jsonFile["varName"] == "isHeatingOn":
                if jsonFile["varValue"] == 1:
                    self.turnOn()
                else:
                    self.turnOff()
            elif jsonFile["varName"] == "maxTemperature":
                self.maxTemp = jsonFile["varValue"]

    def __emmit__(self, varName, varValue):
        msg = {}
        msg["roomName"] = self.roomName
        msg["varName"] = varName
        msg["varValue"] = varValue
        json_msg = json.dumps(msg)
        SocketWrapper().update(json_msg)