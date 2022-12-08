from db import db


class HistoryEventModel(db.Model):
    __tablename__ = "history_event"

    id = db.Column(db.Integer, primary_key=True, index=True)
    event_id = db.Column(db.Integer, db.ForeignKey("event.id"))
    status = db.Column(db.String(80))
    date_time = db.Column(db.String(80))
    

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_all(cls):
        return cls.query.all()