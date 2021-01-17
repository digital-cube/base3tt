from tortoise.models import Model
from tortoise import fields


class App(Model):
    class Meta:
        table = "app"

    id = fields.UUIDField(pk=True)
    test = fields.TextField(null=True)
