import json
import uuid
from Utility.Encryptor import Encryptor
from Utility.color_print import ColorPrint
from flaskapp import db, app
from flask import request, Response, send_file, send_from_directory, make_response, session
from sqlalchemy import tuple_
from sqlalchemy.dialects.postgresql import JSON
import datetime

from DBModel.DB_Product import DB_Product
from DBModel.DB_User import DB_User


class Shop():

	@staticmethod
	def add_to_cart():
		new_items = request.get_json()
		ColorPrint.print_message('Debug', '/add_to_cart', 'Add to cart.')

		if 'cart' not in session.keys():
			#there's no cart yet
			ColorPrint.print_message('Debug', '/add_to_cart', 'Cart was not in session.')
			session['cart'] = []

		cart = session['cart']

		for new_item in new_items:
			#iterate through new items
			already_in_cart = False
			for item in cart:
				if new_item["name"] == item["name"] and new_item["color"] == item["color"]:
					already_in_cart = True
					item["quantity"] += new_item["quantity"]
			if not already_in_cart:
				cart += [{'name': new_item["name"], 'color': new_item["color"], 'quantity': new_item["quantity"]}]
		session.modified = True
		dict_local={'code':200}
		return_string = json.dumps(dict_local, sort_keys=True, indent=4, separators=(',', ': '))
		return return_string

	@staticmethod
	def delete_cart():
		if 'cart' not in session.keys():
			dict_local = {'code': 31, 'message': "No cart exists anyways."}
			return_string = json.dumps(dict_local, sort_keys=True, indent=4, separators=(',', ': '))
			return return_string
		else:
			#in this situation, the session does have the cart
			session['cart'] = None
			session.modified = True
			dict_local = {'code': 200}
			return_string = json.dumps(dict_local, sort_keys=True, indent=4, separators=(',', ': '))
			return return_string


	@staticmethod
	def get_cart():
		if 'cart' in session.keys():
			cart = session['cart']
		else:
			cart = {}
			return_string = json.dumps(cart, sort_keys=True, indent=4, separators=(',', ': '))
			return return_string

		item_tuples = []
		for item in cart:
			item_tuples += [(item["name"], item["color"])]

		products = DB_Product.query.filter(tuple_(DB_Product.name, DB_Product.color).in_(item_tuples)).all()

		arr_local = []

		for product in products:
			prod_dict = {}
			prod_dict["name"] = product.name
			prod_dict["image"] = product.primary_image
			prod_dict["price"] = product.price
			prod_dict["max_qty"] = product.stock
			prod_dict["color"] = product.color

			for item in cart:
				if item["name"] == product.name and item["color"] == product.color:
					prod_dict["quantity"] = item["quantity"]
			
			arr_local += [prod_dict]

		return_string = json.dumps(arr_local, sort_keys=True, indent=4, separators=(',', ': '))
		return return_string

	@staticmethod
	def get_cart_size():
		if 'cart' in session.keys():
			cart_size = 0
			for product in session['cart']:
				cart_size += product["quantity"]
		else:
			cart_size = 0

		return_string = json.dumps(cart_size, sort_keys=True, indent=4, separators=(',', ': '))
		return return_string

	@staticmethod
	def add_product():

		if 'user' in session.keys():
			user = session['user']
			if DB_User.query.filter_by(email = user["email"]).first().account_type == "admin":
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
			else:
				dict_local = {'code': 37, 'message': "Permission error " + cookie["email"]}
				return_string = json.dumps(dict_local, sort_keys=True, indent=4, separators=(',', ': '))
				return return_string
		else:
			dict_local = {'code': 31, 'message': "auth error"}
			return_string = json.dumps(dict_local, sort_keys=True, indent=4, separators=(',', ': '))
			return return_string

	@staticmethod
	def edit_product():
		#this is for changing the product
		parsed_json = request.get_json()

		name = parsed_json["name"]
		color = parsed_json["color"]

		#after this it needs changing...
		new_values = parsed_json["new_values"]

		#get the record
		product_info = DB_Product.query.filter(DB_Product.name == name, DB_Product.color == color).first()

		if product_info is None:
			dict_local={'code':31, 'message':'no product of this description'}
			return_string = json.dumps(dict_local, sort_keys=True, indent=4, separators=(',', ': '))
			return return_string


		if "stock" in new_values:
			product_info.stock = new_values["stock"]
		if "price" in new_values:
			product_info.price = new_values["price"]
		if "primary_image" in new_values:
			product_info.primary_image = new_values["primary_image"]
		if "description" in new_values:
			product_info.description = new_values["description"]
			product_info.details = new_values["details"]

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
app.add_url_rule('/edit_product', 'edit_product', Shop.edit_product, methods=['POST'])
app.add_url_rule('/get_cart', 'get_cart', Shop.get_cart, methods=['GET'])
app.add_url_rule('/get_cart_size', 'get_cart_size', Shop.get_cart_size, methods=['GET'])
app.add_url_rule('/add_to_cart', 'add_to_cart', Shop.add_to_cart, methods=['POST'])
app.add_url_rule('/delete_cart', 'delete_cart', Shop.delete_cart, methods=['POST'])

