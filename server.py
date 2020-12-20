from flask import Flask
from flask import json
from flask import render_template 
from flask_socketio import SocketIO

from heater import *
from SocketWrapper import SocketWrapper
from House import House
import tkinterClient

app = Flask(__name__)
app.config['SECRET_KEY'] = 's1ckret'
socketio = SocketIO(app)

@app.route('/')
def hello_world():
    return render_template("controls.html", rooms=House().getConfig()['rooms'])

@socketio.on('message')
def handle_message(message):
    #print('received message: ' + message)
    pass
    
@socketio.on('sync')
def handle_my_custom_event():
    print('Start synchronizing...')
    SocketWrapper().emmit('sync', House().getConfig())
    print('Synchronizing completed.')

@socketio.on('update')
def handle_message(json_msg):
    print('update')
    #print('Receive update from a client: ' + json_msg)
    fileJSON = json.loads(json_msg)
    House().updateValue(fileJSON);
    SocketWrapper().emmit_update(json_msg)
    print('update end')
    #print('Emit update-confirm to a client: ' + json_msg)

@socketio.on('update-confirm')
def handle_message(json):
    print('update-confirm')
    #print('Receive update-confirm from a client: ' + json)

if __name__ == '__main__':
    SocketWrapper().tie(socketio)
    House().setConfig("./cfg/rooms.json")
    House().info()
    threading.Timer(5, tkinterClient.init).start()
    socketio.run(app, debug=False) 
    
    

