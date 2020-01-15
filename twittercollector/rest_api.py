#!flask/bin/python
import graypy
import logging
import json
from flask import Flask, jsonify
from logic_db import *
from mongo_config import *
from flask_cors import CORS, cross_origin

# Get logger
def buildLogging():
    log = logging.getLogger('werkzeug')
    log.setLevel(logging.INFO)
    handler = graypy.GELFUDPHandler('localhost', 12201)
    log.addHandler(handler)

app = Flask(__name__)

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

buildLogging()

# Route from question a
@app.route('/api/show-fls', methods=['GET'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def get_find_fl():
    app.logger.info('info')
    return jsonify(list_aggr_fl)

# Route from question b
@app.route('/api/group-hrs', methods=['GET'])
def get_group_by_hr():
    app.logger.info('info')
    return jsonify(list_aggr_by_hr)


# Route from question c
#@app.route('/api/group-lang', methods=['GET'])
#def get_group_by_lang():
#    return jsonify(logic_db.group_lang)


# This route doesn't exist. 
# This function purposely calls an error (error 500).
@app.route('/api/error', methods=['GET'])
def get_error():
    try:
        return error # Doesn't exist this var
    except NameError:
        app.logger.error('An error occurred.', exc_info=1)



if __name__ == '__main__':
    
    # run REST API
    app.run()
