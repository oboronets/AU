"""
Rocket qt'ed
"""
import flask
from launch import Launch

app = flask.Flask(__name__)

@app.route("/")
def hello_world():
    return flask.render_template('index.html')

@app.route("/murka")
def murka():
    return flask.render_template('murka.html')

@app.route("/lab")
def lab():
    return flask.render_template('lab.html')

@app.route("/rocket")
def rocket_page():
    return flask.render_template('rocket.html', visibility = 'hidden')

@app.route("/rocket/result")
def rocket_result():
    plane_vx = int(flask.request.args.get("plane_vx"))
    plane_vy = int(flask.request.args.get("plane_vy"))
    max_time = int(flask.request.args.get("max_time"))
    rocket_v = int(flask.request.args.get("rocket_v"))

    launch = Launch(plane_vx, plane_vy, max_time, rocket_v)
    podlet = int( launch.launch_rocket() )
    if podlet > 0:
        return flask.render_template('rocket_result.html', visibility='hidden')
    return flask.render_template('rocket.html', visibility='visible')
