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

    def updateValue(self, jsonFile):
        pass

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
                entity = Heater(component['is_on'],
                                component['min'],
                                component['max'],
                                component['now'])
                HeaterWrapper().tie(entity)
            elif component['type'] == 'light_bulb':
                entity = LightBulb(component['is_on'])
            elif component['type'] == 'light_bulb_brightness':
                entity = LightBulbBrightness(component['is_on'], component['now'])

            self.components.append(entity)
