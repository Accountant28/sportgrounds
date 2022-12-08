from ma import ma
from models.history_user_event import HistoryUserEventModel


class HistoryUserEventSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = HistoryUserEventModel
        load_only = "id"
        ordered = True
        load_instance = True
        include_fk = True