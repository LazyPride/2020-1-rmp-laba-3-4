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
        self.socket.emit(topic, json)
        
    def emmit_update(self, json):
        # TODO: Add logging
        self.socket.emit('update', json)
    
    def emmit_update_var(self, id, var_name, var):
        print("[Socket][Emmit]: id: {}, var_name: {}, var: {}".format(id, var_name, var))
        msg = {}
        msg["id"] = id
        msg["var_name"] = var_name
        msg["var_val"] = var
        json_msg = json.dumps(msg)
        self.socket.emit('update', json_msg)
    
    
    def emmit_confirm(self, json):
        # TODO: Add logging
        self.socket.emit('update-confirm', json)