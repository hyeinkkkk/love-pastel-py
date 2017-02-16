from app import db
from app.common import make_plain_dict_list, make_plain_dict


class Answer(db.Model):
    __tablename__ = 'answers'
    id = db.Column(db.Integer, primary_key=True)
    type_a = db.Column(db.String)
    type_b = db.Column(db.String)
    type_a_point = db.Column(db.Float)
    type_b_point = db.Column(db.Float)


def get_all():
    return make_plain_dict_list(Answer.query.filter().order_by(Answer.id).all())


def get(choice_id):
    return make_plain_dict(Answer.query.filter(Answer.id == choice_id).first())