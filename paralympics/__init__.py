import os
from flask import Flask

def create_app(test_config=None):
    # create the Flask app
    app = Flask(__name__, instance_relative_config=True)
    