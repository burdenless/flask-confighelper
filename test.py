from flask import Flask
from flask_config import FlaskConfig

app = Flask(__name__)
FlaskConfig(app)
