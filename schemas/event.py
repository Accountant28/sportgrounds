from marshmallow import Schema, fields


class EventSchema(Schema):
    id = fields.Str(dump_only=True)
    event_name = fields.Str(unique=True)
    description = fields.Str()
    activity_id = fields.Integer()
    owner_id = fields.Integer()
    place_id = fields.Integer()
    start_date_time = fields.DateTime()
    finish_date_time = fields.DateTime()
    count_users = fields.Integer()
    open_invite = fields.Bool(load_default=False)
    add_user_link = fields.Str()
    status = fields.Str()
    online = fields.Bool(load_default=False)
    type_id = fields.Integer()