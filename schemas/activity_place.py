from ma import ma
from models.activity_place import ActivityPlaceModel


class ActivityPlaceSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ActivityPlaceModel
        ordered = True
        load_instance = True
        include_fk = True