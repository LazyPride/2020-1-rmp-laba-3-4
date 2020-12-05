import threading

class Heater:
    def __init__(self, roomName, curTemp, maxTemp):
        self.roomName = roomName
        self.curTemp = curTemp
        self.maxTemp = maxTemp
        self.isOn = 0
        
    def turnOn(self):
        self.isOn = 1
        print("The heater in {} is On({}) to {} degrees".format(self.roomName, self.isOn, self.maxTemp))
        
    def turnOff(self):
        self.isOn = 0
        print("The heater in {} is Off({})".format(self.roomName, self.isOn))

heater_map = {}

def heaterInit(json):
    global heater_map
    for room in json:
        heater_map[room["roomName"]] = Heater(room["roomName"], room["temperature"], room["maxTemperature"])
        if room["isHeatingOn"] == 1:
            heater_map[room["roomName"]].turnOn()
        else:
            heater_map[room["roomName"]].turnOff()

            

def heaterUpdate(json):
    global heater_map
    print(heater_map)
    if json["varName"] == "isHeatingOn":
        if json["varValue"] == 1:
            print("I AM ON")
            heater_map[json["roomName"]].turnOn()
        else:
            print("I AM OFF")
            heater_map[json["roomName"]].turnOff()
    elif json["varName"] == "maxTemperature":
        heater_map[json["roomName"]].maxTemp = json["varValue"]
    