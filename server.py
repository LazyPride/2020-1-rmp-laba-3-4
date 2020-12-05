from flask import Flask
from flask import json
from flask import render_template 
from flask_socketio import SocketIO

from heater import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 's1ckret'
socketio = SocketIO(app)
fileJSON = ''

def startDummyHeaterThread():
    global heater_map
    print("Heater controller start")
    threading.Timer(1.0, startDummyHeaterThread).start()
    for heater in heater_map.values():
        
        if heater.isOn == 1:
            if int(heater.curTemp) >= int(heater.maxTemp):
                heater.turnOff()
            else:
                if int(heater.curTemp) < 100:
                    heater.curTemp = heater.curTemp + 1
        else:
            if heater.curTemp > 0:
                heater.curTemp = heater.curTemp - 1
        msg = {}
        msg["roomName"] = heater.roomName
        msg["varName"] = "temperature"
        msg["varValue"] = heater.curTemp
        json_msg = json.dumps(msg)
        socketio.emit('update', json_msg)

        msg["roomName"] = heater.roomName
        msg["varName"] = "isHeatingOn"
        msg["varValue"] = heater.isOn
        json_msg = json.dumps(msg)
        print(json_msg)
        socketio.emit('update', json_msg)
        

@app.route('/')
def hello_world():
    # TODO: Handle exception if file not found
    file = open("./cfg/rooms.json")
    fileStr = file.read()
    # TODO Logging without print method
    print(fileStr)
    global fileJSON
    fileJSON = json.loads(fileStr)
    print(fileJSON)
    heaterInit(fileJSON)
    startDummyHeaterThread()
    return render_template("controls.html", rooms=fileJSON)

@socketio.on('message')
def handle_message(message):
    print('received message: ' + message)

@socketio.on('sync')
def handle_my_custom_event():
    print('Start synchronizing...')
    global fileJSON
    socketio.emit('sync', fileJSON)
    print('Synchronizing completed.')

@socketio.on('update')
def handle_message(json_msg):
    print('Receive update from a client: ' + json_msg)
    fileJSON = json.loads(json_msg)
    heaterUpdate(fileJSON);
    socketio.emit('update-confirm', json_msg)
    print('Emit update-confirm to a client: ' + json_msg)

@socketio.on('update-confirm')
def handle_message(json):
    print('Receive update-confirm from a client: ' + json)

if __name__ == '__main__':
    socketio.run(app, debug=True) 
    
    

