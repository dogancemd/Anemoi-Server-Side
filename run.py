from flask import Flask, request


application = Flask(__name__)

from app.modules.bearing.controller import *




if(__name__ == '__main__'):
    application.run("0.0.0.0", port=8000, debug=False)