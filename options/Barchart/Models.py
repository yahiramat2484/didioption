from options.extensions import db
from sqlalchemy import text
from sqlalchemy.dialects.postgresql import JSONB
from options.common.models import SaveMixin


class Barchart(db.Model, SaveMixin):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(JSONB, nullable=False)
    time_stamp = db.Column(db.DateTime,  server_default=text('now()'))


