
from flask import Flask, session
from flask import request

from flaskapp import app, db

from API.Newsletter import Newsletter
from API.Shop import Shop
from API.User import User

#db.drop_all()
db.create_all()

@app.after_request
def apply_caching(response):
    response.headers["Access-Control-Allow-Credentials"] = "true"
    return response

if __name__ == '__main__':
   app.run(host="0.0.0.0", port=5001)
