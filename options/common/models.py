from sqlalchemy.exc import DataError
from options.extensions import db

class SaveMixin(object):
    """Provides the default implementation of the save method"""

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
        except DataError:
            db.session.rollback()


    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except DataError:
            db.session.rollback()