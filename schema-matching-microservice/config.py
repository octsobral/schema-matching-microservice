from os import getenv

import load_env
load_env.load()


class Config:

    API = ''
    VERSION = '0.0.0'

    HOST = getenv('HOST')
    APP_PORT = int(getenv('APP_PORT')) if getenv('APP_PORT') else ""
    #DEBUG = eval(getenv('DEBUG').title()) if getenv('DEBUG') else ""
    #LOGS_PATH = path.abspath(getenv('LOGS_PATH')) if getenv('LOGS_PATH') else ""

    DOCUMENT_DATABASE = getenv('USER_API_DATABASE')
    DATABASE_HOST = getenv('DATABASE_HOST')
    DATABASE_PORT = int(getenv('DATABASE_PORT')) if getenv('DATABASE_PORT') else ""
    DATABASE_USERNAME = getenv('DATABASE_USERNAME')
    DATABASE_PASSWORD = getenv('DATABASE_PASSWORD')

class DevelopmentConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True

class TestingConfig(Config):
    FLASK_ENV = 'testing'
    DEBUG = True
    CA_MOCK_SERVICES = False

class HomologationConfig(Config):
    FLASK_ENV = 'production'
    DEBUG = False

class ProductionConfig(Config):
    FLASK_ENV = 'production'
    DEBUG = False


config = {
    'development': DevelopmentConfig,
    'dev': DevelopmentConfig,
    'testing': TestingConfig,
    'homologation': HomologationConfig,
    'hml': HomologationConfig,
    'production': ProductionConfig,
    'prd': ProductionConfig,
    'default': DevelopmentConfig
}


def get_current_config():
    return config[getenv('FLASK_ENV', 'default').lower()]()