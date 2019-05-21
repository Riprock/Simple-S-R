import os

from flask import Flask

def create_app(test_config=None): #Application factory function
    """This creates and configures the app"""
    app = Flask(__name__, instance_relative_config=True)#Creates flask instance
    app.config.from_mapping(SECRET_KEY='dev', DATABASE=os.path.join(app.instance_path, 'simple.sqlite'),)#Sets Where the database is and what the secret key is

    if test_config is None:
        """This loads the instance config if it exists when the program is not testing"""
        app.config.from_pyfile('config.py', silent=True)#overides default config with the values set in config.py, can be used to generate real secret keys
    else:
        """if config is not none, load test config"""
        app.config.from_mapping(test_config)
    try:
        """Verify that the isntance folder exists"""
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    def page():
        return "GOOD MORNING"
    return app