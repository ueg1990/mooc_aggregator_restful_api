'''
Hello World example in flask
'''

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    '''
    Hello world function
    '''
    return 'Hello World!!!'


if __name__ == '__main__':
    # Enable debug mode so that server restarts everytime there is a change to
    # a file. Remove in production
    app.run(debug=True)
    # app.run()
