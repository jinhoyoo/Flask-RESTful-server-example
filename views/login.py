
#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Reference: https://github.com/maxcountryman/flask-login/wiki/A-simple-working-demo
from flask import Blueprint,flash,url_for,redirect,request,current_app,render_template, send_from_directory,session
from werkzeug.security import generate_password_hash,check_password_hash
import json

#Database interface
from model import UserDBHandler

Login = Blueprint( 'login', __name__)

@Login.route('/login', methods=['POST'])
def login_handler():

    if 'POST' == request.method:
        #To-Do: Implement the log in process.
        return render_template('data_studio_main.html')
