from flask import Flask
from flask_config import FlaskConfig
from dotenv import load_dotenv

load_dotenv('.env')
app = Flask(__name__)
FlaskConfig(app, config_mod='example_config', env_file='.env')

print app.config['DATABASE_URI']
