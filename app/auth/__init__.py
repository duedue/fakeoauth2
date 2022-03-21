# -*- coding: utf-8 -*-
# app/common/__init__.py
import traceback

from flask import current_app as app
from flask import request
from flask_restful import Api, Resource, reqparse
from flask_login import login_user, current_user, logout_user

from app.response import success, error, notfound, unauth

class Auth(Resource):

    def get(self):
        app.logger.info(request.args if request.method in ('GET', ) else request.form)
        parser = reqparse.RequestParser()
        parser.add_argument('client_id', type=str, required=True)
        parser.add_argument('redirect_uri', type=str, required=True)
        parser.add_argument('state', type=str, required=True)
        parser.add_argument('scope', type=str, required=True)
        parser.add_argument('response_type', type=str, required=True)
        parser.add_argument('user_locale', type=str, required=True)
        args = parser.parse_args()

        return success()

class Token(Resource):

    def post(self):
        app.logger.info(request.args if request.method in ('GET', ) else request.form)
        parser = reqparse.RequestParser()
        parser.add_argument('client_id', type=str, required=True)
        parser.add_argument('client_secret', type=str, required=True)
        parser.add_argument('grant_type', type=str, required=True)
        parser.add_argument('code', type=str, required=True)
        parser.add_argument('redirect_uri', type=str, required=True)
        parser.add_argument('refresh_token', type=str, required=True)
        args = parser.parse_args()

        return success()

class Callback(Resource):

    def post(self):
        app.logger.info(request.args if request.method in ('GET', ) else request.form)

        return success()

class auth(object):

    @staticmethod
    def init_app(app):
        app.logger.info('?')
        api = Api()
        api.add_resource(Auth, '/a/v1/authorize', endpoint='auth-v1')
        api.add_resource(Token, '/a/v1/token', endpoint='token-v1')
        api.add_resource(Callback, '/a/v1/callback', endpoint='callback-v1')
        api.init_app(app)

