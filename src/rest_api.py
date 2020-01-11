#!flask/bin/python
#from logic_db import *
import json
from flask import Flask, jsonify
from src import logic_db
from flask_cors import CORS, cross_origin

app = Flask(__name__)

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


@app.route('/api/show-fls', methods=['GET'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def get_find_fl():
    return jsonify(logic_db.json_format_fl)

@app.route('/api/group-hrs', methods=['GET'])
def get_group_by_hr():
    return jsonify(logic_db.group_list_by_hours)

#@app.route('/api/group-lang', methods=['GET'])
#def get_group_by_lang():
#    return jsonify(logic_db.group_lang)

