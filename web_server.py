#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Configurations
import config

import logging
from logging.handlers import RotatingFileHandler

from flask import Flask,redirect,url_for,session,render_template, Blueprint
from flask_restful import Api, Resource, url_for
from flask.ext.pymongo import PyMongo
from flask.ext.cors import CORS

#Blue prints for RESTful API.
from modules import User,Folder

#Blue prints for view of page.
from views import Login,Logout,Signup


#Initialize.
app = Flask(__name__)

#CORS: To allow for accessing other server's request for RESTful API.
CORS(app)


# use for encrypt session
app.config['SECRET_KEY'] = 'HHYz96HNJ9NTFb'

#Add blueprint modules for RESTful API.
api_bp = Blueprint('api', __name__)
api = Api(api_bp, serve_challenge_on_401=True)

# Add more handler for resource.
api.add_resource( User, '/v1/user', '/v1/user/<string:user_id>')
api.add_resource( Folder, '/v1/folder', '/v1/folder/<string:folder_id>')

#Add blueprint modules on flask app.
app.register_blueprint(api_bp)

#Add blue print modules for general views.
app.register_blueprint(Login)
app.register_blueprint(Signup)
app.register_blueprint(Logout)


#Add index page.
@app.route('/')
def index():
    if 'username' in session:
        #To-Do: Implement the function when user is logged in.
        return render_template( 'data_studio_main.html', user_name=user_name)
    else:
        #To-Do: Implement the function when user is nog logged in.
        return redirect('/login')


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True )
