#!flask/bin/python
#from logic_db import *
import json
from flask import Flask, jsonify
from logic_db import *




app = Flask(__name__)

tasks = [
    #five_most_followers

# "[{\"_id\": \"5e12739d04834073e102b00b\", \"user_name\": \"Kirk Borne\", \"followers_count\": 251076}, {\"_id\": \"5e12739f04834073e102b03d\", \"user_name\": \"IBM Developer\", \"followers_count\": 98018}, {\"_id\": \"5e1273a204834073e102b08e\", \"user_name\": \"MIO \\u7c73\\u6b50\", \"followers_count\": 78178}, {\"_id\": \"5e12739c04834073e102afeb\", \"user_name\": \"Sebastien Meunier\", \"followers_count\": 52651}, {\"_id\": \"5e12739d04834073e102b001\", \"user_name\": \"Hacker Noon\", \"followers_count\": 52462}]"
    
    
    
]

@app.route('/api', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})


if __name__ == '__main__':
    app.run(debug=True)
    
