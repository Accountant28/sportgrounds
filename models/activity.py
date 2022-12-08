from db import db


class ActivityModel(db.Model):
    __tablename__ = "activity"

    id = db.Column(db.Integer, primary_key=True, index=True)
    name = db.Column(db.String(80))
    category = db.Column(db.String(80))

    activity_id = db.relationship("ActivityPlaceModel", backref=db.backref("activity"), lazy="dynamic")


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()