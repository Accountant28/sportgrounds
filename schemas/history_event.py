from ma import ma
from models.history_event import HistoryEventModel


class HistoryEventSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = HistoryEventModel
        ordered = True
        load_instance = True
        include_fk = True