from ma import ma
from models.place import PlaceModel


class PlaceSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = PlaceModel
        ordered = True
        load_instance = True