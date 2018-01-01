import json
import uuid
from Utility.Encryptor import Encryptor
from Utility.color_print import ColorPrint
from flaskapp import db, app
from flask import request, Response, send_file, send_from_directory, make_response
from sqlalchemy.dialects.postgresql import JSON
import datetime
import mailchimp
from mailchimp import ListAlreadySubscribedError 


class Shop():

	@staticmethod
	def get_products():
		
		parsed_json = request.get_json()

		email = parsed_json["email"]

		dict_local = {'code': 200}
		
		return_string = json.dumps(dict_local, sort_keys=True, indent=4, separators=(',', ': '))
		return return_string 

app.add_url_rule('/get_products', 'get_products', Shop.get_products, methods=['GET'])
