"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

from flask import Flask
import importlib

app = Flask(__name__)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app


@app.route('/')
def hello():
    """Renders a sample page."""
    return "Hello World!"

@app.route('/packages')
def packages():
    packages = ['pandas', 'matplotlib', 'numpy', 'pygame', 'flask', 'django', 'requests', 'scipy']
    for package in packages:
	    try:
		    var = importlib.import_module(package)
		    print('Package ' + package + ' OK' + '</br>')
	    except ModuleNotFoundError:
		    print('Package ' + package + ' not found' + '</br>')

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
