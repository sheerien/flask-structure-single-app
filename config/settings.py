import os

class Config:
    """ basic confugrations"""
    DEBUG = False
    PORT = os.environ.get('PORT') or 5000
    ENV = os.environ.get('FLASK_ENV')
    FLASK_APP = os.environ.get('FLASK_APP')


class development(Config):
    """ development confugrations"""
    DEBUG = True


class production(Config):
    """ production confugrations"""
    PORT = os.environ.get('PORT') or 8080