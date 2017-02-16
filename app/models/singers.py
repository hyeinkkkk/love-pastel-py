from app import db


class Singer(db.Model):
    __tablename__ = 'singers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
