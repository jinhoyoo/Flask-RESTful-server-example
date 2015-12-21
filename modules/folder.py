import json
from flask import Flask, Blueprint, request, current_app
from auth import AuthResource


class Folder(AuthResource):
    """
    Class for folder resource management.
    """

    def get(self, folder_id):
        #To-Do: Implement GET for folder resource.
        folder_entity = None: #To-Do: Create folder entity in the DB.
        if None == folder_entity:
            return "Wrong request by wrong ID.", 404

        folder_entity.pop("_id")
        folder_entity[u"href"] = request.url
        return folder_entity, 200

    def delete(self, folder_id):
        #To-Do: Implement GET for folder resource.
        folder_entity = None #To-Do: Delete folder entity in the DB.
        if None == folder_entity:
            return "Wrong request by wrong ID.", 404
        else:
            deleted_num = folder_db.delete(folder_id)
            if 1 == deleted_num:
                return {"href": request.url}, 200
        return {}, 404

    def post(self, folder_id=None):
        if folder_id == None:
            return self.__post_without_id()
        else:
            return self.__post_with_id(folder_id)

    def __post_with_id(self, folder_id):
        #To-Do: Update folder entity.
        data = request.json

        if 0 == len(data):
            return {"msg": "No data in JSON."}, 404

        try:
            # To-Do: Update folder_entity.
        except:
            return {"msg": "Server error by wrong request."}, 404

        # Return updated folder entity.
        try:
            # To-Do: reformat JSON data to return.
            updated_folder_entity = None #To-Do: Query from DB.
            return updated_folder_entity, 200
        except:
            return {"msg": "No update of folder entity"}, 404

    def __post_without_id(self):
        #To-Do: Create folder entity.
        data = request.json

        if 0 == len(data):
            return "No data in JSON.", 404
        try:
            rs = None
            #To-Do: Create folder in the DB.
            return rs, 201
        except:
            return {"msg": "Fail to create folder entity."}, 404
