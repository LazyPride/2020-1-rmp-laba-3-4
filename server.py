from flask import Flask
from flask import json
from flask import render_template 
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 's1ckret'
socketio = SocketIO(app)
fileJSON = ''

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
    return render_template("controls.html", rooms=fileJSON)

@socketio.on('message')
def handle_message(message):
    print('received message: ' + message)

@socketio.on('sync')
def handle_my_custom_event():
    print('Start synchronizing...')
    global fileJSON
    socketio.emit('sync', fileJSON)

@socketio.on('update')
def handle_message(json):
    print('Value updated on client: ' + json)
    socketio.emit('update-confirm', json)

@socketio.on('update-confirm')
def handle_message(json):
    print('Value updated on server confirmed: ' + json)


if __name__ == '__main__':
    socketio.run(app, debug=True) 