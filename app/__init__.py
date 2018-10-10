import os

from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

import config

# Flask application
application = Flask(__name__)

# Set app config
if 'PRODUCTION' in os.environ:
    config = config.Production
    application.config.from_object('config.Production')
else:
    config = config.Debug
    application.config.from_object('config.Debug')
    print('App is running in debug mode.')

# SQLAlchemy database
db = SQLAlchemy(application)

# Login manager settings
login_manager = LoginManager()
login_manager.init_app(application)
login_manager.login_view = "login"

# Include models and routes
from app.database import models
from app import routes

# Do any other app initialization here
