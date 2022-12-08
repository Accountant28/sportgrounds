from ma import ma
from models.type_event import TypeEventModel


class TypeEventSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = TypeEventModel
        ordered = True
        load_instance = True