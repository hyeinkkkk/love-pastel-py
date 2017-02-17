from app import db
from app.common import make_plain_dict_list, make_plain_dict, create_or_update_query


class PlayerTemperatures(db.Model):
    __tablename__ = 'playerTemperatures'
    id = db.Column(db.Integer, primary_key=True)
    temperature = db.Column(db.Float)


def add(temper):
    p_t = PlayerTemperatures(temperature=temper)
    return create_or_update_query(p_t)
