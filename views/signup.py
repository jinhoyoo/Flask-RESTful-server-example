#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Reference: https://github.com/maxcountryman/flask-login/wiki/A-simple-working-demo
from flask import Blueprint, flash, redirect, url_for, \
    render_template, send_from_directory, \
    get_flashed_messages, request, current_app


from model import UserDBHandler, signup_user

@Signup.route('/signup', methods=['GET', 'POST'])
def sign_up_handler():
    user_set = UserDBHandler(current_app).list_of_users()

    if 'GET' == request.method:
        #To-Do: Open the page to sign up.
        return render_template('signup.html', result=user_set)
    else:
        #To-Do: Register the user in the database.

        e_mail = request.form['email']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        password = request.form['password']

        #To-Do: Put user into database.

        if user_id == None:
            flash("Already registered user")
            return render_template('signup.html', result=user_set)
        else:
            flash("Succeed to register user.")
            return render_template('signup.html', result=user_set)

        return render_template('signup.html', result=user_set)
