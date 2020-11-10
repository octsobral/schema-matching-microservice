import uuid
from datetime import datetime

import mongoengine as mongo


class Document(mongo.DynamicDocument):

    id = mongo.UUIDField(primary_key=True, default=uuid.uuid4)
    source = mongo.StringField(required=True)
    timestamp = mongo.DateTimeField(required=True, default=datetime.utcnow, editable=False)

    #meta = {
    #    'collection': 'documents',
    #    'strict': False,
    #    'allow_inheritance': True
    #}