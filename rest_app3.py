
from flask import Flask, request
from db_connector import *
import os
import signal

app = Flask(__name__)


# supported methods
@app.route('/users/<id>')
def user(id):
    try:
        name = get_id(id)
        if name == '':
            raise Exception
        else:
            return {'status': 'ok', 'user name': name}, 200
    except:
        return {'status': 'error', 'reason': "No such id"}, 500  # status code


@app.route('/')
def health_check():
    return "200"

@app.route('/stop_server')
def stop_server():
    os.kill(os.getpid(), signal.SIGINT)
    return 'Server stopped'


app.run(host='0.0.0.0')
