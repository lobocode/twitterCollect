#!flask/bin/python
import time
import graypy
import logging
import json
import prometheus_client


# My modules
from collect_data import CollectData
from logic_db import *
from mongo_config import *

# Flask
from flask import Flask, jsonify, request, Response
from flask_cors import CORS, cross_origin
from flask_graylog import Graylog

# Prometheus metrics
from metrics import setup_metrics


# Flask app name
app = Flask(__name__)

# setup metrics
setup_metrics(app)

# Graylog
graylog = Graylog(app)

# Get logger with graylog handler
handler = graypy.GELFUDPHandler('graylog', 12201)
logger = logging.getLogger(__name__)
logger.addHandler(graylog.handler)

# Log to graylog
graylog.info('Message', extra={
    'extra': 'metadata',
})

# Cors authorization
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

# Content type
CONTENT_TYPE_LATEST = str('text/plain; version=0.0.4; charset=utf-8')

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


# Prometheus metrics
@app.route('/metrics/')
def metrics():
    return Response(prometheus_client.generate_latest(), mimetype=CONTENT_TYPE_LATEST)


if __name__ == '__main__':

    # run REST API
   app.run('0.0.0.0', 5000)
   
