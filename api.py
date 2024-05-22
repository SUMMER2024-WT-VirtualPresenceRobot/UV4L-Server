from flask import Flask, redirect, url_for, jsonify, request
from flask_cors import CORS
import robot_control  

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True, headers=['Content-Type', 'Authorization'])
robot = robot_control.RobotControl()

@app.route('/')
def index():
    return '''
    <form action="http://10.13.233.31:5000/forward" method="post">
        <input type="submit" value="Forward" style="height:120px; width:120px" />
    </form>
    '''

@app.route('/forward', methods=['POST'])
def forward():
    robot.forward()
    return redirect('http://10.13.233.31:8888/')

@app.route('/backward', methods=['POST'])
def backward():
    robot.backward()
    return redirect('http://10.13.233.31:8888/')

@app.route('/strafe_left', methods=['POST'])
def strafe_left():
    robot.strafe_left()
    return redirect('http://10.13.233.31:8888/')

@app.route('/strafe_right', methods=['POST'])
def strafe_right():
    robot.strafe_right()
    return redirect('http://10.13.233.31:8888/')

@app.route('/turn_left', methods=['POST'])
def turn_left():
    robot.turn_left()
    return redirect('http://10.13.233.31:8888/')

@app.route('/turn_right', methods=['POST'])
def turn_right():
    robot.turn_right()
    return redirect('http://10.13.233.31:8888/')

@app.route('/stop', methods=['POST'])
def stop():
    robot.stop()
    return redirect('http://10.13.233.31:8888/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
