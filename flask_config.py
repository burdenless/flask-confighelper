#from flask_dotenv import load_dotenv
from os import environ

class FlaskConfig(object):

    def __init__(self, app=None, config_file=None):
        self.app = app
        if app is not None:
            self.init_app(app, config_file)

    def init_app(self, app, config_file):
        if config_file is None:
            app.config['CONFIG_FILE'] = 'config'
        else:
            app.config['CONFIG_FILE'] = config_file

        self.load_config()

    def load_config(self):
        cfg = self.app.config['CONFIG_FILE']
        module = __import__(cfg)
        for mod in dir(module):
            if 'Config' in mod:
                obj = getattr(module,mod)
                for item in dir(obj):
                    if item[0:2] != '__':
                        var = getattr(obj, item)
                        try:
                            self.check_required(var)
                        except ValueError:
                            print "Error. {} is required".format(item)

    def check_required(self, var):
        if var == 'required':
            raise ValueError
        
