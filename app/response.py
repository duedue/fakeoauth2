# -*- coding: utf-8 -*-
# app/janus/response.py
from flask import make_response, jsonify
from flask import current_app as app
from datetime import datetime


def response_datetime():
    return datetime.now().strftime('%Y/%m/%d %H:%M:%S')

def success(key=None, data=None):
    if key:
        err = errorMsg.get(key)
        if data:
            resp = {**dict(result=False, code=err.get('code'), response=response_datetime()), **data}
        else:
            resp = dict(result=False, code=err.get('code'), response=response_datetime())

        return make_response(jsonify(resp), 200)
    else:
        if data:
            return make_response(jsonify({**dict(result=True, response=response_datetime()), **data}), 200)

        return make_response(jsonify(result=True, response=response_datetime()), 200)

def error(key, data=dict()):
    err = errorMsg.get(key)

    resp = jsonify({**dict(code=err.get('code'), response=response_datetime()), **data})

    return make_response(resp, 400)

def unauth(key='LOGIN_REQUIRED'):
    err = errorMsg.get(key)

    return make_response(jsonify(code=err.get('code'), response=response_datetime()), 401)

def notfound(key):
    err = errorMsg.get(key)

    return make_response(jsonify(code=err.get('code'), response=response_datetime()), 404)

class errorMsg(object):
    msg = dict()
    
    @classmethod
    def get(cls, id):
        if id in cls.msg:
            return cls.msg.get(id)
        
        return {'code': -1, 'msg': 'Unknown code.'}
