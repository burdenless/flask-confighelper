# Flask Config
Helper utility to manage Flask app configuration. FlaskConfig checks that the necessary ENVIRONMENT
variables are present, and loads them into the app config.

## Installation
`pip install flask-config`

## Usage
```
from flask import Flask
from flask_config import FlaskConfig

app = Flask(__name__)
FlaskConfig(app, config_module='example_config')

print app.config['DATABASE_URI']
```
