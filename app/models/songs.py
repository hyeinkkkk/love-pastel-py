from datetime import datetime
from app import db
from app.common import make_plain_dict_list


class Song(db.Model):
    __tablename__ = 'songs'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    singer_id = db.Column(db.Integer, db.ForeignKey('singers.id'))
    lyric = db.Column(db.String)
    type_id = db.Column(db.Integer, db.ForeignKey('types.id'))


def get_all():
    return make_plain_dict_list(Song.query.filter().all())


