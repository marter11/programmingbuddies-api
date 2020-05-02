"""
This script runs the api application using a development server.
"""

from os import environ
from api import app

if __name__ == '__main__':
    # Host is '0.0.0.0' instead of 'localhost' because we want to be able to reach it in the Docker container
    HOST = '0.0.0.0'
    try:
        PORT = int(environ.get('SERVER_PORT', '5001'))
    except ValueError:
        PORT = 5001
    if environ.get('FLASK_ENV', 'production') == 'development':
        app.run(HOST, PORT, ssl_context=('cert.pem', 'key.pem'))
    else:
        app.run(HOST, PORT)
