import marshmallow as ma


class LoginRequestSchema(ma.Schema):
    email = ma.fields.Email()
    password = ma.fields.String()


class Login200ResponseSchema(ma.Schema):
    message = ma.fields.String()
    user_id = ma.fields.Int()


class Login401ResponseSchema(ma.Schema):
    error = ma.fields.String()


class UsersCreateRequestSchema(ma.Schema):
    name = ma.fields.String()
    lastname = ma.fields.String()
    email = ma.fields.Email()
    phone = ma.fields.String()
    password = ma.fields.String()


class UsersCreate200ResponseSchema(ma.Schema):
    message = ma.fields.String()
    user_id = ma.fields.Int()


class UsersCreate400ResponseSchema(ma.Schema):
    error = ma.fields.String()
