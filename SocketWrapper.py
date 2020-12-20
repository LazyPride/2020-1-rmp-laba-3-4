from flask import Flask
from flask import json
from flask_socketio import SocketIO

class SocketWrapper(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(SocketWrapper, cls).__new__(cls)
        return cls.instance
        
    def tie(self, socket):
        self.socket = socket
        
    def emmit(self, topic, json):
        self.socket.emmit(topic, json)
        
    def emmit_update(self, json):
        # TODO: Add logging
        self.socket.emmit('update', json)
    
    def emmit_confirm(self, json):
        # TODO: Add logging
        self.socket.emmit('update-confirm', json)