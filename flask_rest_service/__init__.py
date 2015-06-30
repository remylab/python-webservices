import json
from flask import Flask
from flask.ext import restful
from flask import make_response

app = Flask(__name__)

def output_json(data, code, headers=None):
    resp = make_response(json.dumps(data), code)
    resp.headers.extend(headers or {})
    return resp
    
DEFAULT_REPRESENTATIONS = {'application/json': output_json}
api = restful.Api(app)
api.representations = DEFAULT_REPRESENTATIONS

import flask_rest_service.resources