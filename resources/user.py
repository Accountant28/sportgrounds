import uuid
from flask import request, jsonify
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask_jwt_extended import (create_access_token,
                                jwt_required,
                                get_jwt,
                                set_access_cookies,
                                unset_jwt_cookies)

from models.user import UserModel
# from models.event import EventModel
# from models.history_user_event import HistoryUserEventModel
# from models.owner import OwnerModel

from schemas.user import UserSchema, GetUserSchema, LoginUserSchema, ConfirmUserSchema
# from schemas.owner import OwnerSchema
# from schemas.event import EventSchema
# from schemas.history_user_event import HistoryUserEventSchema

from passlib.hash import pbkdf2_sha256
# from datetime import datetime

from sqlalchemy.exc import SQLAlchemyError

from blocklist import BLOCKLIST

# user_schema = UserSchema()
# owner_schema = OwnerSchema()
# event_schema = EventSchema()
# history_user_event_schema = HistoryUserEventSchema()
# list_history_user_event_schema = HistoryUserEventSchema(many=True)


blp = Blueprint("Users", __name__, description="Operations with users")


@blp.route("/user/register")
class User(MethodView):
    @blp.arguments(UserSchema)
    @blp.response(201, UserSchema)
    def post(self, user_data):
        """
        Create new user
        """
        user = UserModel(**user_data)

        if UserModel.find_by_email(user.email):
            abort(409, message='A user with this email already exists')

        hashed_password = pbkdf2_sha256.hash(user.password)
        user.password = str(hashed_password)

        try:
            # owner.save_to_db()
            # user.owner_id = owner.id
            user.code = user.send_sms_confirmation()
            user.save_to_db()
            return {"message": "Account created successfully, code has been sent to your phone number"}
        except SQLAlchemyError:
            abort(500, message="Internal server error. Failed to create user")
        return {"message": "Account created successfully, code has been sent to your phone number"}


@blp.route("/user/login")
class UserLogin(MethodView):
    @blp.arguments(LoginUserSchema)
    def post(self, user_data):
        """
        User login
        """
        user_data = UserModel(**user_data)
        user = UserModel.find_by_email(user_data.email)

        if user.email and pbkdf2_sha256.verify(user_data.password, user.password):
            if user.activated:
                access_token = create_access_token(identity=user.id, fresh=True)
                return {"access_token": access_token}
            abort(400, message="You have not confirmed registration, please check your phone")
        abort(400, message="Invalid email or password")


@blp.route('/user/logout')
class UserLogout(MethodView):  # Для OPENAPI метод не обязателен
    @jwt_required()
    def post(self):
        jwt = get_jwt()["jti"]
        BLOCKLIST.add(jwt)
        return {"message": "You are successfully logged out"}


@blp.route('/user/<int:user_id>')
class User(MethodView):
    @jwt_required()
    @blp.response(200, GetUserSchema)
    def get(self, user_id):
        """
        Get user by id
        """
        user = UserModel.find_by_id(user_id)
        if not user:
            abort(404, message="User not found")
        return user


@blp.route('/user/confirm_registration/<int:user_id>')
class UserConfirm(MethodView):
    @blp.arguments(ConfirmUserSchema)
    def post(self, user_data, user_id):
        user_data = UserModel(**user_data)
        user = UserModel.find_by_id(user_id)

        if not user:
            abort(400, message="User not found")
        if user.code == user_data.code:
            user.activated = True
            user.save_to_db()
            return {"message": "Your registration has been confirmed"}
        abort(400, "Invalid credentials")

# class JoinToEventWaiting(Resource):
#     """
#     User, by user's id, joins to event by event's id with status "wating".
#     And then makes an entry in history user event database
#     if user has not joined to event yet with status "waiting".
#     """

#     @classmethod
#     @jwt_required()
#     def post(cls, event_id, user_id):

#         event = EventModel.find_by_id(event_id)
#         user = UserModel.find_by_id(user_id)
#         history_user_event_model = HistoryUserEventModel()

#         if not event:
#             return {"message": "Event with this id does not exist"}

#         if not user:
#             return {"message": "User with this id does not exist"}

#         history_user_event_model.user_id = user.id    
#         history_user_event_model.event_id = event.id  
#         history_user_event_model.status = "waiting" 
#         history_user_event_model.date_time = datetime.now().strftime("%m/%d/%Y %H:%M:%S")  


#         history = list_history_user_event_schema.dump(HistoryUserEventModel.find_all())
#         events = [item for item in history if event_id == item["event_id"]]

#         count_users = []
#         for one_event in events:
#             dict_of_events = dict(one_event)
#             if (
#                 dict_of_events["user_id"] == user_id
#                 and dict_of_events["status"] == "waiting"
#             ):
#                 count_users.append(user_id)
#         if len(count_users) >= 1:
#             return {"message": "You have already joined to this event"}

#         try:
#             history_user_event_model.save_to_db()
#             return {"message": "You are saccessfully joined to event"}
#         except:
#             return {"message": "User can't join to this event"}, 500


# class JoinToEventApproved(Resource):
#     """
#     User, by user's id, joins to event by event's id with status "approved".
#     And then makes an entry in history user event database
#     if user has not joined to event yet with status "approved".
#     """

#     @classmethod
#     @jwt_required()
#     def post(cls, event_id, user_id):

#         event = EventModel.find_by_id(event_id)
#         user = UserModel.find_by_id(user_id)
#         history_user_event_model = HistoryUserEventModel()

#         if not event:
#             return {"message": "Event with this id does not exist"}

#         if not user:
#             return {"message": "User with this id does not exist"}

#         history_user_event_model.user_id = user.id    
#         history_user_event_model.event_id = event.id  
#         history_user_event_model.status = "approved" 
#         history_user_event_model.date_time = datetime.now().strftime("%m/%d/%Y %H:%M:%S")


#         history = list_history_user_event_schema.dump(HistoryUserEventModel.find_all())
#         events = [item for item in history if event_id == item["event_id"]]

#         count_users = []
#         for one_event in events:
#             dict_of_events = dict(one_event)
#             if (
#                 dict_of_events["user_id"] == user_id
#                 and dict_of_events["status"] == "approved"
#             ):
#                 count_users.append(user_id)
#         if len(count_users) >= 1:
#             return {"message": "You have already joined to this event"}

#         try:
#             history_user_event_model.save_to_db()
#             return {"message": "You are saccessfully joined to event"}
#         except:
#             return {"message": "User can't join to this event"}, 500
