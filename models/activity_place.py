from db import db


class ActivityPlaceModel(db.Model):
    __tablename__ = "activity_place"

    id = db.Column(db.Integer, primary_key=True, index=True)
    activity_id = db.Column(db.Integer, db.ForeignKey("activity.id"))
    place_id = db.Column(db.Integer, db.ForeignKey("place.id"))
    rating_activity_place = db.Column(db.Float(precision=2), default=0)


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_all(cls):
        return cls.query.all()