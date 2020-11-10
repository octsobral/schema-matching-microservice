from flask_restful import Resource
from flasgger import swag_from
from flask import request
from werkzeug import exceptions

import definitions
from service.file_upload_service import FileUploadService
from model.file_upload.file_upload_request import FileUploadRequest


class FileUploadController(Resource):

    def __init__(self):
        self.file_upload_service = FileUploadService()

    @swag_from(definitions.ROOT_DIR + "/swagger/models/file_upload/file-upload.yml", endpoint="file_upload")
    def get(self):

        try:
            file = request.files['file']
            name = request.values['name']
        except exceptions.BadRequestKeyError as err:
            raise err

        file_upload_request = FileUploadRequest(file, name)
        file_upload_response = self.file_upload_service.file_upload(file_upload_request)

        return file_upload_response.to_json()
