from db import db


class OwnerModel(db.Model):
    __tablename__ = "owner"

    id = db.Column(db.Integer, primary_key=True, index=True)
    raiting_owner = db.Column(db.Integer, default=0)
    

    @classmethod
    def find_all(cls):
        return cls.query.all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()