from os import environ


class DefaultConfig(object):
    HOST = "localhost"
    DATABASE = environ["DATABASE"]
    DB_USER = environ["DB_USER"]
    DB_PASS = environ["DB_PASS"]
    DB_PORT = 5432
    SQLALCHEMY_DATABASE_URI = 'postgresql://' + DB_USER + ':' + DB_PASS + \
                              '@{0}:{1}/{2}'.format(HOST, DB_PORT, DATABASE)

    SQLALCHEMY_TRACK_MODIFICATIONS = False