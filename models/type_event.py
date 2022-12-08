from db import db


class TypeEventModel(db.Model):
    __tablename__ = "type_event"

    id = db.Column(db.Integer, primary_key=True, index=True)
    name = db.Column(db.String(80))

   
    def save_to_db(self):
        db.session.bulk_save_objects(self)
        db.session.commit()

    @classmethod
    def find_all(cls):
        return cls.query.all()