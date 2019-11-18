# import  app
class Config(object):

    DEBUG = True
    SECRET_KEY = "this-is-secret-by-kibet"
    SQLALCHEMY_DATABASE_URI = "mysql://root@localhost/kibet"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

