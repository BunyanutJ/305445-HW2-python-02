from flask import Flask , request
from flask_restful import Resource ,Api,reqparse
import json
from werkzeug.datastructures import FileStorage

app = Flask (__name__)

api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('img', type=FileStorage, location='files')

class UploadFile(Resource):
	def get(self):
		return {"message":"Plese sent 'img' (POST method) to me."}
	def post(self):
		args = parser.parse_args()
		image = args['img']
		image_name = image.filename
		image.save(image_name)
		return {"code":200,"desc":"upload success"}
		
api.add_resource(UploadFile,'/')
if __name__ == '__main__':
	app.run(host='0.0.0.0',port=5500)

