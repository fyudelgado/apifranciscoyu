from marshmallow import fields

from app.ext import ma


class ProfileSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    username = fields.String()
    image_url = fields.String()
    type = fields.String()
    link = fields.String()
