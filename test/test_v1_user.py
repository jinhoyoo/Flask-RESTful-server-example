#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_v1_user.py
~~~~~~~~~~~~~~~

Test cases for datalibs system's RESTful API and simple view.

Reference: https://flask-testing.readthedocs.org/en/latest/#installing-flask-testing
"""

import os,sys,unittest,json
sys.path.append('../')

from flask import Flask
from flask.ext.testing import TestCase
from werkzeug.datastructures import Headers
import datetime
import dateutil.parser

from webserver_test import BaseDataLibsTestCase
import config, model



class V1UserTestCase(BaseDataLibsTestCase):


    def test_create_user_entity(self):
        user_data = {
            u"e_mail": u"iu@loen.com",  #User’s e-mail. It will be used as user ID.
            u"firstName":u"Jieun", #Encrypted password.
            u"lastName":u"Lee",
            u"password":u"1234",
            u"rootFolder": u"http://localhost/v1/folder/19ad1239sdqweop", #_id of folder object.
            u"sharedRootFolder": [] #_id of shared folder object.
        }

        user_id = self.create_user( \
            user_data["e_mail"], \
            user_data["firstName"], \
            user_data["lastName"], \
            user_data["password"], \
            user_data["rootFolder"] )

        #GET to test whether user is created or not.
        rv = self.client.get( \
            '/v1/user/'+str(user_id),\
            headers=self.get_basic_header()
            )

        self.assert200(rv,rv.json)

        #Check data.
        self.assertIn( "e_mail", rv.json )
        self.assertIn( "firstName", rv.json )
        self.assertIn( "lastName", rv.json )
        self.assertIn( "rootFolder", rv.json )
        self.assertIn( "sharedFolderSet", rv.json )
        self.assertIn( "href", rv.json )


        #POST to creat user. Have to fail!
        new_user_data = {
            u"e_mail": u"iu@loen.com",  #User’s e-mail. It will be used as user ID.
            u"firstName":u"Jieun", #Encrypted password.
            u"lastName":u"Lee",
            u"password":u"4132112sdfa",
            u"rootFolder": u"http://localhost/v1/folder/19afasd1239sdqweop", #_id of folder object.
            u"sharedRootFolder": [] #_id of shared folder object.
        }

        rv = self.client.post( \
            '/v1/user', \
            data=new_user_data, \
            headers=self.get_basic_header()
            )

        self.assert404(rv,rv.json)


if __name__ == '__main__':
    unittest.main()
