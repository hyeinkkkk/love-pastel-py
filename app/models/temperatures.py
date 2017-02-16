from app import db
from sqlalchemy import and_
from app.common import make_plain_dict

class Temperature(db.Model):
    __tablename__ = 'temperatures'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String)
    range_start = db.Column(db.Float)
    range_end = db.Column(db.Float)


def get(value):
    return make_plain_dict(Temperature.query.filter(and_(Temperature.range_start <= value, Temperature.range_end > value)).first())
