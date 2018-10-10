import os

# Project base dir
basedir = os.path.abspath(os.path.dirname(__file__))


# Common configurations
class Common:
    DEBUG = True
    WTF_CSRF_ENABLED = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    UNAUTHORIZED_MESSAGE = "You don't have authorization to perform this action."

    # Enter a secret key
    SECRET_KEY = 'my-secret-key'


# Debug specific configurations
class Debug(Common):
    # Enter your local database name
    SQLALCHEMY_DATABASE_URI = 'mysql://root@localhost:3306/sampledb'


# Production specific configurations
class Production(Common):
    DEBUG = False
    env = os.environ
    # Database configuration
    SQLALCHEMY_DATABASE_URI = 'mysql://' + str(env.get('DB_USER')) + ':' + str(env.get('DB_PASS')) + '@' + \
                              str(env.get('DB_HOST')) + '/' + str(env.get('DB_SCHEMA'))
