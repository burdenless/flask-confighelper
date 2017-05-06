class Config(object):
    DATABASE_URI = 'optional'
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
