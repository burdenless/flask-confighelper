from dotenv import load_dotenv
from os import environ

class FlaskConfig(object):

    def __init__(self, app=None, config_file=None):
        try:
            load_dotenv('.env')
            environ['ENVIRONMENT']
        except KeyError:
            print('ENVIRONMENT configuration not found, using default Config')

        self.error_count = 0
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
        try:
            module = __import__(cfg)
        except NameError:
            print("No module named {}".format(cfg))
            exit(1)

        for mod in dir(module):
            if 'Config' in mod:
                obj = getattr(module,mod)
                for item in dir(obj):
                    if item[0:2] != '__':
                        self.check_required(obj, item)
            if self.error_count > 0:
                exit(1)

    def check_required(self, obj, item):
        var = getattr(obj, item)
        if var == 'required':
            try:
                environ[item]
            except KeyError:
                print('Error. {} is required, and was not found.'.format(item))
                self.error_count += 1
