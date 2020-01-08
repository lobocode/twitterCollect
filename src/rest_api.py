#!flask/bin/python
#from logic_db import *
import json
from flask import Flask, jsonify
from logic_db import *


app = Flask(__name__)


tasks = json_format_fl

@app.route('/api', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})


if __name__ == '__main__':
    app.run(debug=True)
    
