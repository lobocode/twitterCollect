#!flask/bin/python
#from logic_db import *
import json
from flask import Flask, jsonify
from src import logic_db

app = Flask(__name__)

tasks = logic_db.json_format_fl

@app.route('/api', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

