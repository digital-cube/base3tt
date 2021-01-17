from tortoise.models import Model
from tortoise import fields


class User(Model):
    class Meta:
        table = "users"

    id = fields.UUIDField(pk=True)
    test = fields.TextField(null=True)
