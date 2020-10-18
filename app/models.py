from app import db
from sqlalchemy.dialects.postgresql import JSON


class Covid(db.Model):
    __tablename__ = 'covid'

    id = db.Column(db.Integer, primary_key=True)
    kitchen = db.Column(db.Boolean)
    bathroom = db.Column(db.Boolean)

    def __init__(self):
        self.kitchen = 0
        self.bathroom = 0

    def __repr__(self):
        return '<id {}>'.format(self.id)
