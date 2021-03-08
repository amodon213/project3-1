from flask import Flask, request
from db_connector import *
import os
import signal

app = Flask(__name__)


# supported methods
@app.route('/users/<id>', methods=['GET', 'POST', 'DELETE', 'PUT'])
def user(sent_id):
    if request.method == 'GET':
        try:
            name = get_id(sent_id)
            if name == '':
                raise Exception
            else:
                return {'status': 'ok', 'user name': name}, 200
        except:
            return {'status': 'error', 'reason': f'No such {sent_id} haha'}, 500  # status code

    elif request.method == 'POST':
        try:
            name = request.json.get('name')
            insert_user(sent_id, name)
            return {'status': 'ok', 'user added': name}, 200  # status code
        except:
            return {'status': 'error', 'reason': 'No such id'}, 500 # status code# status cod

    
    elif request.method == 'PUT':
        try:
            name = request.json.get('name')
            update_user(name, sent_id)
            return {'status': 'ok', 'user_updated': name}, 200  # status code
        except:
            return {'status': 'error', 'reason': 'No such id'}, 500

    elif request.method == 'DELETE':
        try:
            delete_user(sent_id)
            return {'status': 'ok', 'user_deleted': sent_id}, 200  # status code
        except:
            return {'status': 'error', 'reason': 'No such id'}, 500

@app.route('/')
def health_check():
    return "200"

@app.route('/stop_server')
def stop_server():
    os.kill(os.getpid(), signal.SIGINT)
    return 'Server stopped'


app.run(host='0.0.0.0', debug=True, port=5000)
