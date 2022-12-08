from ma import ma
from models.activity import ActivityModel


class ActivitySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ActivityModel
        ordered = True
        load_instance = True