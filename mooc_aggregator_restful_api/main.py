'''
This module will contain all the routes for the restful API
'''

from flask import Flask, make_response, jsonify, request
from mongoengine import connect
from flask.ext.mongoengine import MongoEngine

from models import Mooc

app = Flask(__name__)

# Update this variable everytime a new MOOC platform is added to the Restful API
MOOC_PLATFORMS = {'udacity', 'coursera'}


@app.route('/')
def hello_world():
    '''
    Welcome Page
    '''
    return 'Welcome to the MOOC Aggregator Restful API!!!\n'


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
    Get all MOOCs from the server. Allow retrieving only subset of fields by
    passing subset of fields as GET parameter with key 'fields', for example,

    curl http://127.0.0.1:5000/moocs/api/v1/courses?fields=title,subtitle

    If provided key is other than 'fields' or any value of subset of fields
    does not match that in database, return result of default API call:

    curl http://127.0.0.1:5000/moocs/api/v1/courses


    '''
    fields = request.args.get('fields')
    if fields:
        try:
            parameters = fields.split(',')
            return jsonify({'moocs': Mooc.objects.only(*parameters).to_json()})
        except:
            return jsonify({'moocs': Mooc.objects.to_json()})
    return jsonify({'moocs': Mooc.objects.to_json()})


@app.route('/moocs/api/v1/courses/<mooc>', methods=['GET'])
def get_courses_by_mooc(mooc):
    '''
    Get all courses that belong to a given MOOC platform e.g. Udacity or Coursera
    Allow retrieving only subset of fields by passing subset of fields as GET
    parameter with key 'fields', for example,

    curl http://127.0.0.1:5000/moocs/api/v1/courses/udacity?fields=title,subtitle

    If provided key is other than 'fields' or any value of subset of fields
    does not match that in database, return result of default API call:

    curl http://127.0.0.1:5000/moocs/api/v1/courses/udacity

    '''
    if mooc in MOOC_PLATFORMS:
        fields = request.args.get('fields')
        if fields:
            try:
                parameters = fields.split(',')
                return jsonify({'moocs': Mooc.objects(mooc=mooc).only(*parameters).to_json()})
            except:
                return jsonify({'moocs': Mooc.objects(mooc=mooc).to_json()})
        return jsonify({'moocs': Mooc.objects(mooc=mooc).to_json()})
    else:
        return not_found()


@app.route('/moocs/api/v1/coursenames', methods=['GET'])
def get_coursenames():
    '''
    Get all names of the MOOCs from the server

    '''
    result = [course['title'] for course in Mooc.objects]
    return jsonify({'coursenames': result})


@app.route('/moocs/api/v1/coursenames/<mooc>', methods=['GET'])
def get_coursenames_by_mooc(mooc):
    '''
    Get all coursenames that belong to a given MOOC platform e.g. Udacity or Coursera

    '''
    if mooc in MOOC_PLATFORMS:
        result = [course['title'] for course in Mooc.objects(mooc=mooc)]
        return jsonify({'coursenames': result})
    else:
        return not_found()


@app.route('/moocs/api/v1/courses/<mooc>/<key>', methods=['GET'])
def get_cours_by_mooc_and_key(mooc):
    '''
    Get course info that belong to a given MOOC platform e.g. Udacity or Coursera
    and a key which is unique to the course in the platform. Allow retrieving 
    only subset of fields by passing subset of fields as GET parameter with key 
    'fields', for example,

    curl http://127.0.0.1:5000/moocs/api/v1/courses/udacity?fields=title,subtitle

    If provided key is other than 'fields' or any value of subset of fields
    does not match that in database, return result of default API call:

    curl http://127.0.0.1:5000/moocs/api/v1/courses/udacity/cs101

    '''
    if mooc in MOOC_PLATFORMS:
        fields = request.args.get('fields')
        if fields:
            try:
                parameters = fields.split(',')
                return jsonify({'moocs': Mooc.objects(mooc=mooc, key=key).only(*parameters).to_json()})
            except:
                return jsonify({'moocs': Mooc.objects(mooc=mooc, key=key).to_json()})
        return jsonify({'moocs': Mooc.objects(mooc=mooc, key=key).to_json()})
    else:
        return not_found()


if __name__ == '__main__':

    connect('moocs')
    # Enable debug mode so that server restarts everytime there is a change to
    # a file. Remove in production
    # app.run(debug=True)
    # To make app externally available
    app.run(host='0.0.0.0')
    # app.run()
