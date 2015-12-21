
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Reference: https://github.com/maxcountryman/flask-login/wiki/A-simple-working-demo
from flask import Blueprint, flash, url_for, redirect, request, current_app, render_template, send_from_directory, session
from werkzeug.security import generate_password_hash, check_password_hash

Logout = Blueprint('logout', __name__)


@Logout.route('/logout', methods=['GET'])
def logout_handler():
    #To-Do: Implement function to login out.
    return redirect(url_for('index'))
