from marshmallow import Schema, fields


class UserSchema(Schema):
    id = fields.Str(dump_only=True)
    first_name = fields.Str()
    last_name = fields.Str()
    phone_number = fields.Str()
    email = fields.Str()
    sex = fields.Str()
    level = fields.Str()
    count_completed_events = fields.Str()
    count_money = fields.Float()
    location = fields.Str()
    rating_user = fields.Float()
    owner_id = fields.Str()
    password = fields.Str()
    activated = fields.Bool(load_default=False)
    code = fields.Str()

    class Meta:
        ordered = True


class GetUserSchema(UserSchema):
    class Meta:
        fields = ('id', 'first_name', 'last_name', 'email', 'activated', 'code')
        ordered = True


class LoginUserSchema(UserSchema):
    class Meta:
        fields = ('email', 'password')
        ordered = True


class ConfirmUserSchema(UserSchema):
    class Meta:
        fields = ('id', 'code',)