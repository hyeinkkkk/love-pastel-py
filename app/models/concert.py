from app import db
from app.common import create_or_update_query, make_plain_dict


class Concert(db.Model):
    __tablename__ = 'concert'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    state = db.Column(db.String)

def get():
    return make_plain_dict(Concert.query.filter().first())

def change_state(state):
    concert = Concert.query.filter().first()
    concert.state = state
    return create_or_update_query(concert)