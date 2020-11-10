import uuid
from datetime import datetime

import mongoengine as mongo


class Form(mongo.Document):

    id = mongo.UUIDField(primary_key=True, default=uuid.uuid4)
    uploaded_timestamp = mongo.DateTimeField(required=True)
    file = mongo.FileField(required=True)
    name = mongo.StringField(required=True)

    meta = {
        'collection': 'form_files',
        'strict': False
    }
