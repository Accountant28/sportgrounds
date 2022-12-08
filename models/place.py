from db import db


class PlaceModel(db.Model):
    __tablename__ = "place"

    id = db.Column(db.Integer, primary_key=True, index=True)
    name = db.Column(db.String(80))
    manager_id = db.Column(db.Integer)
    city = db.Column(db.String(80))
    address = db.Column(db.String(80))
    coordinate = db.Column(db.String(80))
    description = db.Column(db.Text)
    dressing_room = db.Column(db.Boolean, default=True)
    count_dressing_room = db.Column(db.Integer)
    shower = db.Column(db.Boolean, default=False)
    parking = db.Column(db.Boolean, default=True)

    place_id = db.relationship("ActivityPlaceModel", backref=db.backref("place"), uselist=True)


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()