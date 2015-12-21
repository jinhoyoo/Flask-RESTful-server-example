#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_v1_folder.py
~~~~~~~~~~~~~~~

Test cases for datalibs system's RESTful API and simple view.

Reference: https://flask-testing.readthedocs.org/en/latest/#installing-flask-testing
"""

import os
import sys
import unittest
import json
sys.path.append('../')

from flask import Flask
from flask.ext.testing import TestCase
from werkzeug.datastructures import Headers
import datetime
import dateutil.parser

from webserver_test import BaseDataLibsTestCase
import config
import model


class V1FolderTestCase(BaseDataLibsTestCase):

    """
     Test cases for "~/v1/folder" API version 1.
    """

    def test_create_folder(self):

        # Create folder entity and jsonize.
        folder_data = {
            u"name": u"hello_folder",
            u"description": u"test_folder creation"
        }

        # POST to create entity.
        rv = self.create_folder(folder_data)

        # Check HTTP response code.
        self.assertEqual(201, rv.status_code, rv.json)

    def test_get_folder(self):

        # Create folder entity and jsonize.
        folder_data = {
            u"name": u"hello_folder_2",
            u"description": u"test_folder creation"
        }

        # POST to create entity.
        rv = self.create_folder(folder_data)

        # Check HTTP response code.
        self.assertEqual(201, rv.status_code, rv.json)

        # Get folder entity
        url_request = rv.json["location"].replace("http://localhost", "")

        rv = self.client.get(
            url_request,
            headers=self.get_basic_header()
        )

        # Check HTTP response code.
        self.assert200(rv, rv.json)

    def test_update_folder(self):

        # Create folder entity and jsonize.
        folder_data = {
            u"name": u"hello_folder_2",
            u"description": u"test_folder creation"
        }

        # POST to create entity.
        rv = self.create_folder(folder_data)

        # Check HTTP response code.
        self.assertEqual(201, rv.status_code, rv.json)

        # Update data
        url_request = rv.json["location"].replace("http://localhost", "")

        # POST to update folder entity.
        new_folder_data = {
            u"name": u"hello_folder_3",
            u"description": u"update folder description2",
            u"projectSet": ["051972zApsofjas1", "pozd12dzApsofja4s"],
            u"childrenFolder": ["051972zApsofjas1", "pozd12dzApdassofja4s"]
        }
        new_json_data = json.dumps(new_folder_data)

        rv = self.client.post(
            url_request,
            data=new_json_data,
            headers=self.get_basic_header()
        )

        # Check HTTP response code.
        self.assert200(rv, rv.json)

        # Check data.
        self.assertIn("name", rv.json)
        self.assertIn("description", rv.json)
        self.assertIn("projectSet", rv.json)
        self.assertIn("childrenFolder", rv.json)
        self.assertIn("share", rv.json)
        self.assertIn("href", rv.json)

        for k in new_folder_data.keys():
            self.assertEqual(new_folder_data[k], rv.json[k])

    def test_delete_folder(self):

        # Create folder entity and jsonize.
        folder_data = {
            u"name": u"hello_folder_2",
            u"description": u"test_folder creation"
        }

        # POST to create entity.
        rv = self.create_folder(folder_data)

        # Check HTTP response code.
        self.assertEqual(201, rv.status_code, rv.json)

        # Delete folder element.
        url_request \
            = rv.json["location"].replace("http://localhost", "")
        rv = self.client.delete(
            url_request,
            headers=self.get_basic_header()
        )

        # Check HTTP response code.
        self.assert200(rv, rv.json)

        # Get to access deleted resource.
        rv = self.client.get(
            url_request,
            headers=self.get_basic_header()
        )

        # Check HTTP response code. Have to be 404.
        self.assert404(rv, rv.json)
