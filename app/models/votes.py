from datetime import datetime
from app import db
from app.common import create_or_update_query


class Vote(db.Model):
    __tablename__ = 'votes'
    id = db.Column(db.Integer, primary_key=True)
    player_id = db.Column(db.Integer, db.ForeignKey('players.id'))
    song_id = db.Column(db.Integer, db.ForeignKey('songs.id'))
    priority = db.Column(db.Integer)
    create_time = db.Column(db.DateTime, default=datetime.now)


def add(player_id, song_id, priority):
    vote = Vote(player_id=player_id,
                song_id=song_id,
                priority=priority)
    return create_or_update_query(vote)