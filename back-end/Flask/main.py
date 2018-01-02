
from flask import Flask
from flask import request

from flaskapp import app, db

from API.Newsletter import Newsletter
from API.Shop import Shop

#db.drop_all()
db.create_all()

if __name__ == '__main__':
   app.run(host="0.0.0.0", port=5001)
