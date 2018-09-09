from os import environ

class Development(object):
    # Get the app root path
    #       <basedir>
    # ../../--> champtrade/Champtrade/config/config.py

    DEBUG = True
    TESTING = False
    # Security
    # This is the secret key that is used for session signing
    # os.urandom(24)
    SECRET_KEY = environ["secret"]

    # Mail
    MAIL_SERVER = 'smtp.1and1.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USER_SSL = False
    MAIL_USERNAME = 'yahir.amat@champtrade.com'
    MAIL_PASSWORD = environ["MAIL_PASSWORD"]
    MAIL_DEFAULT_SENDER = ("Default Sender", "yahir.amat@champtrade.com")
    # Where to logger should send the emails to
    ADMINS = ['yahir.amat@champtrade.com']