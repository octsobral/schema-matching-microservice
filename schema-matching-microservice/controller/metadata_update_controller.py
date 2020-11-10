from flask import request
from flask_restful import Resource
from flasgger import swag_from
from werkzeug import exceptions

import definitions
from model.metadata_update.metadata_update_request import MetadataUpdateRequest
from service.metadata_update_service import MetadataUpdateService


'''

Frontend will show metadata extracted from the file uploaded then it will ask for the user to rename those metadata; new 
metadata will then be available in this endpoint for update

'''

class MetadataUpdateController(Resource):

    def __init__(self):

        self.metadata_update_service = MetadataUpdateService()

    @swag_from(definitions.ROOT_DIR + "/swagger/models/health_check/health-check.yml", endpoint="metadata_update")
    def get(self):

        try:
            id = request.json['id']
            new_metadata = request.json['metadata']
        except exceptions.BadRequestKeyError as err:
            raise err

        metadata_update_request = MetadataUpdateRequest(id, new_metadata)
        metadata_update_response = self.metadata_update_service.metadata_update(metadata_update_request)

        return metadata_update_response.to_json()
