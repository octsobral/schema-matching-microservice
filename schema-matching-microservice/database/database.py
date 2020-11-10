import mongoengine

from config import get_current_config

client = None


def connect():

    global client

    if not client:
        client = mongoengine.connect(
            db=get_current_config().DOCUMENT_DATABASE,
            host=get_current_config().DATABASE_HOST,
            port=get_current_config().DATABASE_PORT,
            username=get_current_config().DATABASE_USERNAME,
            password=get_current_config().DATABASE_PASSWORD,
            connect=False
        )
