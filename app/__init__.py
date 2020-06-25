from flask import Flask 
from flask_bootstrap import Bootstrap
from config import config_options

bootstrap = Bootstrap()


# Initializing application 
def create_app(config_name):

    app = Flask(__name__)
    #Creating app configurations
    app.config.from_object(config_options[config_name])


    # Initializing Flask extensions 
    bootstrap.init_app(app)

    # Registering  the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    #Setting config
    from .requests import configure_request
    configure_request(app)
    # Will add views and forms 

    return app