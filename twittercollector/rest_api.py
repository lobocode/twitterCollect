#!flask/bin/python

import json
from flask import Flask, jsonify
from logic_db import *
from mongo_config import *
from flask_cors import CORS, cross_origin

app = Flask(__name__)

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route('/api/show-fls', methods=['GET'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def get_find_fl():
    return jsonify(json_format_fl)

@app.route('/api/group-hrs', methods=['GET'])
def get_group_by_hr():
    return jsonify(aggr_by_hr)

#@app.route('/api/group-lang', methods=['GET'])
#def get_group_by_lang():
#    return jsonify(logic_db.group_lang)


if __name__ == '__main__':
    
    # run REST API
    app.run(debug=True)
