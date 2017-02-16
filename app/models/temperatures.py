from app import db


class Temperature(db.Model):
    __tablename__ = 'temperatures'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String)
    range_start = db.Column(db.Float)
    range_end = db.Column(db.Float)


