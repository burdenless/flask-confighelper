from os import environ

class FlaskConfig(object):

    def __init__(self, app=None, config_mod=None, env_file=None):
        self.error_count = 0
        self.config_vars = []
        self.app = app

        if app is not None:
            self.init_app(app, config_mod)

    def init_app(self, app, config_mod):
        try:
            app.config['environment'] = environ['ENVIRONMENT']
        except KeyError:
            print('ENVIRONMENT configuration not found, using default Config')
            app.config['environment'] = ''

        if config_mod is None:
            app.config['CONFIG_MOD'] = 'config'
        else:
            app.config['CONFIG_MOD'] = config_mod

        self.load_config()

    def load_config(self):
        cfg = self.app.config['CONFIG_MOD']
        try:
            module = __import__(cfg)
        except NameError:
            print("No module named {}".format(cfg))
            exit(1)

        mod = self.app.config['environment'].capitalize() + 'Config'
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
                self.set_config(item)
            except KeyError:
                print('Error. {} is required, and was not found.'.format(item))
                self.error_count += 1

    def set_config(self, var):
        self.app.config[var] = environ[var]
