from datetime import datetime
from app import db
from app.common import make_plain_dict


class Type(db.Model):
    __tablename__ = 'types'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)


def get(type_id):
    return make_plain_dict(Type.query.filter(Type.id == type_id).first())