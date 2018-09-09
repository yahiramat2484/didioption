import eventlet

eventlet.monkey_patch()

from flask import Flask
from options.extensions import mail, migrate, login_manager, db
from flask_admin import Admin

app = Flask(__name__)
admin = Admin(app, template_mode="bootstrap3")


def create_app(app, config):
    app.config.from_object("options.Configuration.default.DefaultConfig")
    app.config.from_object(config)
    configure_extension(app)
    return app


def configure_extension(app):

    db.init_app(app)

    mail.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return 1

    from options.Barchart.Models import Barchart
    from options.Barchart import views
    from options.admin import views
