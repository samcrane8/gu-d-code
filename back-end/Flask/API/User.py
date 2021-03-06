import json
import uuid
from Utility.Encryptor import Encryptor
from Utility.color_print import ColorPrint
from flaskapp import db, app
from flask import request, Response, send_file, send_from_directory, make_response, session
from sqlalchemy.dialects.postgresql import JSON
from DBModel.DB_User import DB_User
from DBModel.DB_Session import DB_Session
import datetime

encryptor = Encryptor()
seconds_in_hour = 60*60
session_inactivity_timeout = datetime.timedelta(0, seconds_in_hour * 2)

class User():

    @staticmethod
    def login():

        parsed_json = request.get_json()
        email = parsed_json["email"]
        password = parsed_json["password"]

        if DB_User.authenticate_email_password(email, password):
            #then there's not a good cookie, and we're loggin in.

            user = {'email' : email, 'password' : password}
            session['user'] = user
            session.modified=True
            dict_local = {'code': 200}
            return_string = json.dumps(dict_local, sort_keys=True, indent=4, separators=(',', ': '))
            response = make_response(return_string)  
            return response
        else:
            #not a good cookie and no login.
            dict_local = {'code': 31, 'message': "login failed"}
            return_string = json.dumps(dict_local, sort_keys=True, indent=4, separators=(',', ': '))
            return return_string


    @staticmethod
    def logoff():
        if 'user' not in session.keys():
            dict_local = {'code': 31, 'message': "User not logged in anyways."}
            return_string = json.dumps(dict_local, sort_keys=True, indent=4, separators=(',', ': '))
            return return_string
        else:
            session.pop('user', None)
            session.modified = True
            dict_local = {'code': 200}
            return_string = json.dumps(dict_local, sort_keys=True, indent=4, separators=(',', ': '))
            return return_string


    @staticmethod
    def list_all_users():

        if 'user' in session.keys():
            user = session['user']
            if DB_User.query.filter_by(email = user.email).first().account_type == "admin":
                db_user_devices = DB_User.query.all()
                return_json_list = []
                for report in db_user_devices:
                    dict_local = {'name': report.name,
                                                    'email': report.email,
                                                    'password' : report.password,
                                                    'created_at': str(report.created_at),
                                                    'account_type': report.account_type}

                    return_json_list.append(dict_local)
                return_string = json.dumps(return_json_list, sort_keys=True, indent=4, separators=(',', ': '))
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
    def register_user():
        encrypted_cookie = request.cookies.get('sessionID')
        if DB_User.authenticate_user_cookie(encrypted_cookie):
            parsed_json = request.get_json()
            email = parsed_json["email"]
            password = parsed_json["password"]
            name = parsed_json["name"]
            account_type = parsed_json["account_type"]

            user = DB_User(name, password, email, account_type)
            db.session.add(user)
            db.session.commit()

            return_json = {'code': 200}
            return_string = json.dumps(return_json, sort_keys=True, indent=4, separators=(',', ': '))
            return return_string

        else:
            dict_local = {'code': 31, 'message': "auth error"}
            return_string = json.dumps(dict_local, sort_keys=True, indent=4, separators=(',', ': '))
            return return_string	

app.add_url_rule('/login', 'login', User.login, methods=['POST'])
app.add_url_rule('/logoff', 'logoff', User.logoff, methods=['GET'])
app.add_url_rule('/list_all_users', 'list_all_users', User.list_all_users, methods=['GET'])
app.add_url_rule('/register_user', 'register_user', User.register_user, methods=['POST'])
