#!flask/bin/python
import graypy
import logging
import json
from flask import Flask, jsonify
from logic_db import *
from mongo_config import *
from flask_cors import CORS, cross_origin
from flask_graylog import Graylog


app = Flask(__name__)
graylog = Graylog(app)

# Get logger with graylog handler
handler = graypy.GELFUDPHandler('localhost', 12201)
logger = logging.getLogger(__name__)
logger.addHandler(graylog.handler)

# Log to graylog
graylog.info('Message', extra={
    'extra': 'metadata',
})

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

# Route from question a
@app.route('/api/show-fls', methods=['GET'])
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
def get_find_fl():
    logger.info('info')
    return jsonify(list_aggr_fl)

# Route from question b
@app.route('/api/group-hrs', methods=['GET'])
def get_group_by_hr():
    logger.info('testando aggr by hour')
    # app.logger.info('info')
    return jsonify(list_aggr_by_hr)


# Route from question c
# @app.route('/api/group-lang', methods=['GET'])
# def get_group_by_lang():
#    return jsonify(logic_db.group_lang)


# This route doesn't exist.
# This function purposely calls an error (error 500).
@app.route('/api/error', methods=['GET'])
def get_error():
    logger.error('An occurred error')
    return error  # Doesn't exist this var


if __name__ == '__main__':

    # run REST API
    app.run()
