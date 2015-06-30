import json
from flask import request, abort, make_response
from flask.ext import restful
from flask.ext.restful import reqparse
from flask_rest_service import app, api
import httplib
  
def output_json(data, code, headers=None):
    resp = make_response(json.dumps(data), code)
    resp.headers.extend(headers or {})
    return resp    
    
class Root(restful.Resource):
    def get(self):
        # return {'status':'OK'}
	return make_response("",200)
class Imgflip(restful.Resource):
    def get(self):             
        qs = request.query_string
        createUrl = '/caption_image?username=memegen15478742&password=test' + '&' + qs
        conn = httplib.HTTPSConnection("api.imgflip.com")
        conn.request("GET", createUrl, headers={})
        response = conn.getresponse()
        data = response.read()
        result = json.loads( data )
        if result["success"] == True :
            return make_response('imgflip_jsonp( "' + result["data"]["url"]+ '" )',200)
        else:
            return output_json({'error': result["error_message"]}, 400)

api.add_resource(Root, '/')    
api.add_resource(Imgflip, '/imgflip')
