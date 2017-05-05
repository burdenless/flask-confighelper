class Config(object):
    DATABASE_URI = 'optional'

class ProductionConfig(Config):
    DATABASE_URI = 'required'
    TOKEN = 'required'

class DevelopmentConfig(Config):
    DEBUG = 'optional'

class TestingConfig(Config):
    TESTING = 'required'
