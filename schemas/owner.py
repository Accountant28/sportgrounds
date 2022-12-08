from ma import ma
from models.owner import OwnerModel


class OwnerSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = OwnerModel
        ordered = True
        load_instance = True
        include_fk = True