from flask import Flask
from flask import jsonify
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

with open('tasks.json', 'r') as myfile:
    data=myfile.read()
    obj = json.loads(data)

app.run(debug=True)
@app.route('/todo/getall',methods=['GET'])
def getTasks():
    return jsonify(obj)

@app.route('/todo/create',methods=['POST'])
def createTask():
    return 'Create new task'
@app.route('/todo/update',methods=['UPDATE'])
def updateTask():
    return 'Update Task'
@app.route('/todo/delete',methods=['DELETE'])
def deleteTask():
    return 'Delete task'

if __name__ == '__main__':
   app.run(host="0.0.0.0", port="5000", debug=True)