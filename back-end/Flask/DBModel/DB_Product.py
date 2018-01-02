import json
import uuid
from flaskapp import db, app
from sqlalchemy.dialects.postgresql import JSON
from flask import request, Response, send_file, send_from_directory
from Utility.color_print import ColorPrint
import datetime
from Utility.Encryptor import Encryptor



class DB_Product(db.Model):
    __tablename__ = 'product'
    name = db.Column(db.Text, primary_key=True)
    color = db.Column(db.Text, primary_key=True)
    stock = db.Column(db.Integer)
    price = db.Column(db.Float)

    def __init__(self, name, color, stock, price):
        self.name = name
        self.color = color
        self.stock = stock
        self.price = price

    def __repr__(self):
        return '<id {}>'.format(self.id)