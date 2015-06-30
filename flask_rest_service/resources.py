import json
from flask import request, abort
from flask.ext import restful
from flask.ext.restful import reqparse
from flask_rest_service import app, api

class Root(restful.Resource):
    def get(self):
        return {
            'status': 'OK'
        }

api.add_resource(Root, '/')