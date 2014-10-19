'''
This module will contain all the routes for the restful API
'''

from flask import Flask, make_response, jsonify

app = Flask(__name__)


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

    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    # Enable debug mode so that server restarts everytime there is a change to
    # a file. Remove in production
    app.run(debug=True)
    # app.run()
