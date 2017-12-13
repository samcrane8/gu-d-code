import json
import uuid
from Utility.Encryptor import Encryptor
from Utility.color_print import ColorPrint
from flaskapp import db, app
from flask import request, Response, send_file, send_from_directory, make_response
from sqlalchemy.dialects.postgresql import JSON
import datetime
import mailchimp

API_KEY = "94a8d8be7ab3ccea22c02040be37a978-us17"
LIST_ID = 'df86122232' 

api = mailchimp.Mailchimp(API_KEY)

class Newsletter():

	@staticmethod
	def add_to_newsletter():
		
		parsed_json = request.get_json()

		email = parsed_json["email"]

		api.lists.subscribe(LIST_ID, {'email': email})
		
		dict_local = {'code': 200}
		return_string = json.dumps(dict_local, sort_keys=True, indent=4, separators=(',', ': '))
		return return_string 

app.add_url_rule('/add_to_newsletter', 'add_to_newsletter', Newsletter.add_to_newsletter, methods=['POST'])
