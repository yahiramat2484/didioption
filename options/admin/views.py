from flask_admin.contrib.sqla import ModelView
from options.Barchart.Models import Barchart
from options.extensions import db
from options.app import admin

admin.add_view(ModelView(Barchart, db.session))