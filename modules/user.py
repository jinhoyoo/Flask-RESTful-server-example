#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, Blueprint, request, current_app
from flask_restful import Api, Resource, url_for
from model import UserDBHandler
from auth import AuthResource

class User(AuthResource):
    """
    Class for user resource management.
    """

    def get(self, user_id):
        #To-Do: Implement GET for user resource.
        user_entity = None #To-Do: get user entity from DB.

        if None == user_entity:
            msg = {
                "href": request.url,
                "msg": "Wrong request by wrong ID."
            }
            return msg, 404

        user_entity[u"href"] = request.url
        return user_entity, 200

    def post(self, user_id=None):

        if user_id == None:
            return self.__post_without_id()
        else:
            return self.__post_with_id(user_id)

    def __post_without_id(self):
        return "No contents for this request.", 404

    def __post_with_id(self, user_id):
        #To-Do: Update user information.  
        pass
