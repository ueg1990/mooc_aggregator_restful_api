'''
This module will contain all the routes for the restful API
'''

from flask import Flask, make_response, jsonify
from mongoengine import connect
from flask.ext.mongoengine import MongoEngine

from models import Mooc

app = Flask(__name__)
connect('moocs')

# Update this variable everytime a new MOOC platform is added to the Restful API
MOOC_PLATFORMS = {'udacity', 'coursera'}


@app.route('/')
def hello_world():
    '''
    Hello world function
    '''
    return 'Hello World!!!'


@app.errorhandler(404)
def not_found(error):
    '''
    Add Error 404 Handler

    '''
    return make_response(jsonify({'error': 'Not Found'}), 404)


@app.errorhandler(500)
def internal_server_error(error):
    '''
    Add Error 500 Handler

    '''
    return make_response(jsonify({'error': 'Internal Server Error'}), 500)


@app.route('/moocs/api/v1/courses', methods=['GET'])
def get_courses():
    '''
    Get all MOOCs from the server

    '''
    return jsonify({'moocs': Mooc.objects})


@app.route('/moocs/api/v1/courses/<mooc>', methods=['GET'])
def get_courses_by_mooc(mooc):
    '''
    Get all courses that belong to a given MOOC platform e.g. Udacity or Coursera

    '''
    if mooc in MOOC_PLATFORMS:
        return jsonify({'moocs': Mooc.objects(mooc=mooc)})
    else:
        return not_found()

if __name__ == '__main__':
    # Enable debug mode so that server restarts everytime there is a change to
    # a file. Remove in production
    app.run(debug=True)
    # app.run()
