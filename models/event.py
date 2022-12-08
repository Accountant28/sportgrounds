from db import db
from datetime import datetime


class EventModel(db.Model):
    __tablename__ = "event"

    id = db.Column(db.Integer, primary_key=True, index=True)
    event_name = db.Column(db.String(80), unique=True)
    description = db.Column(db.Text)
    activity_id = db.Column(db.Integer)
    owner_id = db.Column(db.Integer)
    place_id = db.Column(db.Integer)
    start_date_time = db.Column(db.DateTime, default=datetime.now())
    finish_date_time = db.Column(db.DateTime, default=datetime.now())
    count_users = db.Column(db.Integer)
    open_invite = db.Column(db.Boolean, default=True)
    add_user_link = db.Column(db.String(80))
    status = db.Column(db.String(30))
    online = db.Column(db.Boolean, default=False)
    type_id = db.Column(db.Integer)

    # owner = db.relationship("OwnerModel", backref=db.backref("event", uselist=False))
    # place = db.relationship("PlaceModel", backref=db.backref("event", uselist=False))
    # activity = db.relationship("ActivityModel", backref=db.backref("event", uselist=False))
    # type_event = db.relationship("TypeEventModel", backref=db.backref("event", uselist=False))
    # history_event = db.relationship("HistoryEventModel", backref=db.backref("event", uselist=False))
    # history_user_event = db.relationship("HistoryUserEventModel", backref=db.backref("event", uselist=False))


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_all(cls):
        return cls.query.all()

    @classmethod
    def find_by_event_name(cls, event_name):
        return cls.query.filter_by(event_name=event_name).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()