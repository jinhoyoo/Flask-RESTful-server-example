#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_datalibs.py
~~~~~~~~~~~~~~~

Test cases for datalibs system's RESTful API and simple view.

Reference: https://flask-testing.readthedocs.org/en/latest/#installing-flask-testing
"""

import os,sys,unittest,json
import logging, base64
from logging.handlers import RotatingFileHandler

from flask import Flask
from flask.ext.testing import TestCase
from werkzeug.datastructures import Headers
import datetime
import dateutil.parser

from web_server import app
import config


class BaseDataLibsTestCase(TestCase):
    """
    Base class for testing.
    """
    config.TESTING = True

    def create_app(self):
        app.config['TESTING'] = True
        return app


    def create_user(self, e_mail, first_name,
                    last_name, password,
                    root_folder_link):
        #To-Do: Create user in the DB for testing.
        return None

    def create_folder(self,folder_data):
        #POST to create folder entity.
        rv = self.client.post(
            '/v1/folder',
            data=json.dumps(folder_data),
            headers\
                =self.get_basic_header()
            )
        return rv

    def get_basic_header(self):
        h = Headers()
        h.add('Authorization',
             'Basic ' + \
                    base64.encodestring(
                        config.API_KEY+":"+config.API_SECRETE
                        ).replace('\n', '')
            )
        h.add('content-type', 'application/json')
        return h


if __name__ == '__main__':
    unittest.main()
