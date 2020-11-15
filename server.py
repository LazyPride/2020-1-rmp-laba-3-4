from flask import Flask
from flask import json
from flask import render_template 

app = Flask(__name__)
@app.route('/')
def hello_world():
    # TODO: Handle exception if file not found
    file = open("./cfg/rooms.json")
    fileStr = file.read()
    # TODO Logging without print method
    print(fileStr)
    fileJSON = json.loads(fileStr)
    print(fileJSON)
    return render_template("controls.html", rooms=fileJSON)

if __name__ == '__main__':
    app.run(debug=True) 