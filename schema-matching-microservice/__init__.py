from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from flasgger import Swagger
import json_logging

from controller.file_upload_controller import FileUploadController
from controller.metadata_update_controller import MetadataUpdateController

from database import database
from config import config, Config
import definitions

app = Flask('schema-matching-microservice')

app.config['SWAGGER'] = {
    'title': "Schema Matching Microservice",
    'uiversion': 1,
    'description': "Schema Matching Microservice Endpoints"
}

CORS(app)
api = Api(app)
swagger = Swagger(app, template_file=definitions.ROOT_DIR + '/swagger/template.yml')

json_logging.ENABLE_JSON_LOGGING = True
json_logging.init_flask()
json_logging.init_request_instrument(app)


def configure_database():
    database.connect()


def configure_api():
    api.add_resource(FileUploadController, '/file_upload', endpoint='file_upload'),
    api.add_resource(MetadataUpdateController, '/metadata_update', endpoint='metadata_update')


def create_app(config_name):
    app.config.from_object(config[config_name])
    app.config['ERROR_404_HELP'] = False

    configure_api()

    configure_database()

    return app
