from flask import Flask
from flask_smorest import Api
from flask_jwt_extended import JWTManager
from db import db
from blocklist import BLOCKLIST

from resources.user import blp as UserBlueprint

#     User,
#     UserConfirm,
#     UserLogin,
#     UserLogout,
#     JoinToEventWaiting,
#     JoinToEventApproved,
# )
# from resources.event import (
#     CreateEvent,
#     EventsList,
#     EventByName,
#     EventById,
#     ChangeEventStatus,
# )
# from resources.owner import OwnerList
# from resources.history_user_event import HistoryUserEvent, CountUsersInEvent
# from resources.history_event import HistoryEvent
# from resources.place import CreatePlace
# from resources.activity import CreateActivity, AssignActivityPlace
# from resources.type_event import CreateTypeEvent
# from resources.activity_place import ActivityPlace

app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:0505@localhost/sport_grounds'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["API_TITLE"] = "Sports Grounds"
app.config['API_VERSION'] = "v1"
app.config['OPENAPI_VERSION'] = "3.0.3"
app.config['OPENAPI_URL_PREFIX'] = "/"
app.config['OPENAPI_SWAGGER_UI_PATH'] = "/swagger-ui"
app.config['OPENAPI_SWAGGER_UI_URL'] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
app.config['API_SPEC_OPTIONS'] = {
        'security': [{"bearerAuth": []}],
        'components': {
            "securitySchemes":
                {
                    "bearerAuth": {
                        "type": "http",
                        "scheme": "bearer",
                        "bearerFormat": "JWT"
                    }
                }
        }
    }

app.config["JWT_TOKEN_LOCATION"] = ["headers", "cookies"]
app.config["JWT_COOKIE_SECURE"] = False #Will be True in production
app.config["JWT_SECRET_KEY"] = "super-secret"
app.secret_key = 'secret-key'


db.init_app(app)
api = Api(app)
jwt = JWTManager(app)

# @jwt.token_in_blocklist_loader
# def check_if_token_in_blacklist(jwt_header, jwt_payload):
#     app.logger.info(jwt_payload)
#     id_iam_looking_for = jwt_payload['jti']
#     return id_iam_looking_for in BLOCKLIST

# @jwt.expired_token_loader
# def expired_token_callback(jwt_header, jwt_payload):
#     return jsonify({
#                     "description": "The token has expired",
#                     "error": "token_expired"
#                    }), 401

# @jwt.invalid_token_loader
# def invalid_token_callback(error):
#     return jsonify({
#         "description": "Signature verification failed",
#         "error": "invalid_token"
#     }), 401

# @jwt.unauthorized_loader
# def missing_token_callback(error):
#     return jsonify({
#         "description": "Request does not contain an access token",
#         "error": "authorization_required"
#     }), 401

# @jwt.revoked_token_loader
# def revoked_token_callback(jwt_header, jwt_payload):
#     return jsonify({
#         "description": "The token has been revoked",
#         "error": "token_revoked"
#     }), 401


api.register_blueprint(UserBlueprint)
# api.add_resource(User, "/users/<int:user_id>")
# api.add_resource(UserLogin, "/login")
# api.add_resource(UserConfirm, "/user_confirm/<int:user_id>")
# api.add_resource(UserLogout, '/logout')

# api.add_resource(OwnerList, "/owners")

# api.add_resource(CreateEvent, "/create_event")
# api.add_resource(EventsList, "/events")
# api.add_resource(EventByName, "/event/<string:event_name>")
# api.add_resource(EventById, "/event/<int:event_id>")
# api.add_resource(JoinToEventWaiting, "/event/<int:event_id>/join-wating/user/<int:user_id>")
# api.add_resource(JoinToEventApproved, "/event/<int:event_id>/join-approved/user/<int:user_id>")
# api.add_resource(ChangeEventStatus, "/event/<int:event_id>/status/<string:event_status>")

# api.add_resource(HistoryUserEvent, "/history")
# api.add_resource(HistoryEvent, "/history_event/<int:event_id>")

# api.add_resource(CreatePlace, "/create_place")

# api.add_resource(CreateActivity, "/create_activity")
# api.add_resource(AssignActivityPlace, "/assign_activity_place/activity/<int:activity_id>/place/<int:place_id>")

# api.add_resource(CreateTypeEvent, "/create_type")

# api.add_resource(CountUsersInEvent, "/count_users_in_event/<int:event_id>")

# api.add_resource(ActivityPlace, "/history_activity_place")


if __name__ == "__main__":

    @app.before_first_request
    def create_tables():
        db.create_all()

    app.run(debug=True)