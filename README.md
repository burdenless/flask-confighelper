# Flask Config
Helper utility to manage Flask app configuration. FlaskConfig checks that the _required_ config
variables are present, and loads them into the app config. It will also check for _optional_ configs, but will not return an error if they are not present.

## Installation
```
pip install flask-config
```

## Usage
The `flask-config` package will read the `ENVIRONMENT` key currently set, and will use the value of that key to identify which `*Config` object to load

#### app.py
```
from flask import Flask
from flask_config import FlaskConfig

app = Flask(__name__)
FlaskConfig(app, config_module='config')

print app.config['DATABASE_URI']
```

#### config.py
```
class Config(object):
    PORT = 'required'
    OPTIONAL = 'optional'

class ProductionConfig(Config):
    DATABASE_URI = 'required'
    TOKEN = 'required'
    OPTIONAL = 'optional'

class DevelopmentConfig(Config):
    DATABASE_URI = 'required'
    DEBUG = 'optional'
    OPTIONAL = 'optional'

class TestingConfig(Config):
    TESTING = 'required'
```
