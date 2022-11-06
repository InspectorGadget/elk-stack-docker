import os

class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or ''
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ELASTICSEARCH_HOST = str(os.environ.get('ELASTICSEARCH_HOST')) or 'localhost'