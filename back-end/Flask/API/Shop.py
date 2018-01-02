import json
import uuid
from Utility.Encryptor import Encryptor
from Utility.color_print import ColorPrint
from flaskapp import db, app
from flask import request, Response, send_file, send_from_directory, make_response
from sqlalchemy.dialects.postgresql import JSON
import datetime

from DBModel.DB_Product import DB_Product


class Shop():

	@staticmethod
	def get_products():

		# arr_local = [{
	#         "id": 1,
	#         "title": "TEST NAME",
	#         "image": "static/PBD_Linens-58.jpg",
	#         "price": "95",
	#         "max_qty": 20,
	#         "color": "white"
	#       },{
	#         "id": 2,
	#         "title": "GUY NAME",
	#         "image": "static/PBD_Linens-58.jpg",
	#         "price": "95",
	#         "max_qty": 20,
	#         "color": "white"
	#       },{
	#         "id": 3,
	#         "title": "SUP NAME",
	#         "image": "static/PBD_Linens-58.jpg",
	#         "price": "95",
	#         "max_qty": 20,
	#         "color": "white"
	#       }]

		arr_local=[]

		products = DB_Product.query.all()

		for product in products:
			prod_dict = {}
			prod_dict["name"] = product.name
			prod_dict["image"] = "https://s3.amazonaws.com/gudlinens/PBD_Linens-58.jpg"
			prod_dict["price"] = product.price
			prod_dict["max_qty"] = product.stock
			arr_local += [prod_dict]
		
		return_string = json.dumps(arr_local, sort_keys=True, indent=4, separators=(',', ': '))
		return return_string 

app.add_url_rule('/get_products', 'get_products', Shop.get_products, methods=['GET'])
