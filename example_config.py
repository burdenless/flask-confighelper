class Config(object):
    DATABASE_URI = 'optional'

class ProductionConfig(Config):
    DATABASE_URI = 'required'
    TOKEN = 'required'

class DevelopmentConfig(Config):
    DATABASE_URI = 'required'
    DEBUG = 'optional'

class TestingConfig(Config):
    TESTING = 'optional'
