import random
from db import db
from twilio.rest import Client
from sqlalchemy.orm import validates
import re


class UserModel(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, index=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    phone_number = db.Column(db.String(80))
    email = db.Column(db.String(80), nullable=True)
    sex = db.Column(db.String(5))
    level = db.Column(db.Integer)
    count_completed_events = db.Column(db.Integer)
    count_money = db.Column(db.Float(precision=2))
    location = db.Column(db.String(80))
    rating_user = db.Column(db.Float(precision=2))
    owner_id = db.Column(db.Integer)
    password = db.Column(db.String(160))
    activated = db.Column(db.Boolean, default=False)
    code = db.Column(db.String, nullable=True)

    # owner = db.relationship("OwnerModel", backref=db.backref("users", uselist=False))
    # history_user_event = db.relationship("HistoryUserEventModel", backref=db.backref("users", uselist=False))


    # @validates("email")
    # def email_is_not_valid(self, key, email):
    #     email_regex_pattern = re.compile("[\w\.]+@+[\w\.]+\.[\w]+")
    #     if not email_regex_pattern.match(email):
    #         return {"message": "Email not valid"}
    #     return email
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    @classmethod
    def generate_otp(cls):
        return random.randrange(10000, 99999)

    def send_sms_confirmation(self):
        account_sid = "AC0de4c17295259d265d5bf7932d6ed803"
        auth_token = "ffbe2c9a7360de65613f60c04badd542"
        client = Client(account_sid, auth_token)
        otp = self.generate_otp()

    #     # message = client.messages.create(
    #     #     body=str(otp),
    #     #     messaging_service_sid="MGced7f7bd116f690384a4e78881f15e68",
    #     #     to="+375293584205",
    #     # )
        return otp