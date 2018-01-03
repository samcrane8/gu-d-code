import json
import uuid
from flaskapp import db, app
from sqlalchemy.dialects.postgresql import JSON
from flask import request, Response, send_file, send_from_directory
from Utility.color_print import ColorPrint
import datetime
from Utility.Encryptor import Encryptor



class DB_ProductImage(db.Model):
    __tablename__ = 'product'
    image_name = db.Column(db.Text, primary_key=True)
    product_name = db.Column(db.Text, db.ForeignKey('product.name', ondelete = 'CASCADE'))
    product_color = db.Column(db.Text, , db.ForeignKey('product.color', ondelete = 'CASCADE'))

    def __init__(self, name, color, stock, price):
        self.name = name
        self.color = color
        self.stock = stock
        self.price = price

    def __repr__(self):
        return '<id {}>'.format(self.id)