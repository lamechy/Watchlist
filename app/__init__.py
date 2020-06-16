from flask import Flask 
from flask_bootstrap import Bootstrap
from .config import DevConfig
# Initializing application 
app = Flask(__name__, instance_relative_config=True)

#Setting up configurations
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

# Initializing Flask extensions 
bootstrap = Bootstrap(app)

from app import views