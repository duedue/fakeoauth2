# -*- coding: utf-8 -*-
# app/__init__.py
import os
from datetime import datetime

from flask import Flask
from flask import current_app as app
from flask_restful import Api

from .config import config
from .auth import auth

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    app.secret_key = 'fakeoauth2'

    auth.init_app(app)

    return app
