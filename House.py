from flask import Flask
from flask import json
from flask_socketio import SocketIO

class House(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(House, cls).__new__(cls)
        return cls.instance
        
    def setConfig(self, cfg_path : str):
        file = open(cfg_path)
        fileStr = file.read()
        self.config = json.loads(fileStr)
       
    def updateValue(self, jsonFile):
        pass
        
    def getConfig(self):
        return self.config