from flask import Flask
from flask_config import FlaskConfig
from dotenv import load_dotenv

load_dotenv('.env')
app = Flask(__name__)
FlaskConfig(app, config_module='example_config')

print app.config['DATABASE_URI']
print app.config['DEBUG']
