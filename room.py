from flask import Flask
from flask import json

from ABCs import *
from light_bulb import LightBulb
from light_bulb_brightness import LightBulbBrightness
from heater import Heater
from HeaterWrapper import HeaterWrapper


class Room(object):
    
    def __init__(self, json_cfg):
        self.config = json_cfg
        self.room_name = self.config['room_name']
        self.components = []
        self.__parse_components(self.config['components'])
        
    def getName(self):
        return self.room_name
        
    def updateValue(self, json_cfg):
        if self.room_name != json_cfg['room_name']:
            return
        
        for component in self.components:
            if component.id == json_cfg['id']:
                component.update_value(json_cfg['value_name'], json_cfg['value'])
        
    def getConfig(self):
        return self.config
        
    def info(self):
        print("[Room]:")
        print("\t name:" + self.config['room_name'])
        for component in self.components:  
            component.info()

    def __parse_components(self, components):
        for component in components:  
            entity = Component()
            if component['type'] == 'heating':
                entity = Heater(component['id'],
                                component['is_on'],
                                component['min'],
                                component['max'],
                                component['now'])
                HeaterWrapper().tie(entity)
                entity.start(1.0)
            elif component['type'] == 'light_bulb':
                entity = LightBulb(component['id'], component['is_on'])
            elif component['type'] == 'light_bulb_brightness':
                entity = LightBulbBrightness(component['id'], component['is_on'], component['now'])
            
            self.components.append(entity)
