import marshmallow as ma


class LoginSchema(ma.Schema):
    email = ma.fields.Email()
    password = ma.fields.String()


class UserCreateRequestSchema(ma.Schema):
    name = ma.fields.String()
    lastname = ma.fields.String()
    email = ma.fields.Email()
    phone = ma.fields.String()
    password = ma.fields.String()


class UserSchema(UserCreateRequestSchema):
    id = ma.fields.Number()
    created_at = ma.fields.String()


class ContactCreateRequestSchema(ma.Schema):
    name = ma.fields.String()
    lastname = ma.fields.String()
    email = ma.fields.Email()
    topic = ma.fields.String()
    message = ma.fields.String()


class ContactSchema(ContactCreateRequestSchema):
    id = ma.fields.Number()
    created_at = ma.fields.String()


class ErrorResponseSchema(ma.Schema):
    error = ma.fields.String()
