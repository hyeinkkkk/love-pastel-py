from datetime import datetime
from app import db
from app.common import create_or_update_query, make_plain_dict


class Player(db.Model):
    __tablename__ = 'players'
    id = db.Column(db.Integer, primary_key=True)
    gender = db.Column(db.String)
    age = db.Column(db.Integer)
    type_id = db.Column(db.Integer, db.ForeignKey('types.id'), default=None)
    create_time = db.Column(db.DateTime, default=datetime.now)
    update_time = db.Column(db.DateTime)


def add(age, gender):
    player = Player(gender=gender, age=age)
    create_or_update_query(player)
    return player
