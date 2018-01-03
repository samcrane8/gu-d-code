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
	def add_product():
		parsed_json = request.get_json()

		name = parsed_json["name"]
		color = parsed_json["color"]
		stock = parsed_json["stock"]
		price = parsed_json["price"]
		primary_image = parsed_json["primary_image"]
		description = parsed_json["description"]
		details = parsed_json["details"]

		product = DB_Product(name, color, stock, price, primary_image, description, details)
		db.session.add(product)
		db.session.commit()

		dict_local={'code':200}
		return_string = json.dumps(dict_local, sort_keys=True, indent=4, separators=(',', ': '))
		return return_string

	@staticmethod
	def get_products():
		dict_local={}

		products = DB_Product.query.all()

		for product in products:
			prod_dict = {}
			prod_dict["name"] = product.name
			prod_dict["image"] = product.primary_image
			prod_dict["price"] = product.price
			prod_dict["max_qty"] = product.stock
			prod_dict["color"] = product.color
			if product.name in dict_local.keys():
				dict_local[product.name] += [prod_dict]
			else:
				dict_local[product.name] = [prod_dict]
		
		return_string = json.dumps(dict_local, sort_keys=True, indent=4, separators=(',', ': '))
		return return_string

	@staticmethod
	def get_product_info():
		parsed_json = request.get_json()

		name = parsed_json["name"]
		color = parsed_json["color"]

		product_info = DB_Product.query.filter(DB_Product.name == name, DB_Product.color == color).first()

		if product_info is None:
			dict_local={'code':31, 'message':'no product of this description'}
			return_string = json.dumps(dict_local, sort_keys=True, indent=4, separators=(',', ': '))
			return return_string

		dict_local={}
		dict_local["images"] = [product_info.primary_image]
		dict_local["price"] = product_info.price
		dict_local["description"] = product_info.description
		dict_local["details"] = product_info.details

		return_string = json.dumps(dict_local, sort_keys=True, indent=4, separators=(',', ': '))
		return return_string


app.add_url_rule('/get_products', 'get_products', Shop.get_products, methods=['GET'])
app.add_url_rule('/get_product_info', 'get_product_info', Shop.get_product_info, methods=['POST'])
app.add_url_rule('/add_product', 'add_product', Shop.add_product, methods=['POST'])


