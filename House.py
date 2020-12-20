from flask import Flask
from flask import json
from room import Room

class House(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(House, cls).__new__(cls)
        return cls.instance
        
    def setConfig(self, cfg_path : str):
        file = open(cfg_path)
        fileStr = file.read()
        self.config = json.loads(fileStr)
        self.rooms = []
        for room_cfg in self.config['rooms']:
            room = Room(room_cfg)
            self.rooms.append(room)
       
    def info(self):
        print("[HOUSE]:")
        for room in self.rooms:
            room.info()
   
    def updateValue(self, jsonFile):
        pass
        
    def getConfig(self):
        return self.config