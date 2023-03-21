from tortoise import Model, fields
from pydantic import BaseModel
from datetime import datetime
from tortoise.contrib.pydantic import pydantic_model_creator


class User(Model):
    nik = fields.IntField(pk=True, index=True)
    nama = fields.CharField(max_length=20, null=False, unique=True)
    no_rekening = fields.CharField(max_length=200, null=False, unique=True)
    no_hp = fields.IntField(null=False)
    is_verified = fields.BooleanField(default =False)
    join_data = fields.DatetimeField(default = datetime.utcnow)

class Rekening(Model):
    nominal = fields.IntField(null=False)
    saldo = fields.IntField(null=False)
    no_rekening = fields.ForeignKeyField("models.User", related_name="tabung")




user_pydantic = pydantic_model_creator(User, name = "User", exclude=("is_verified", ))
user_pydanticIn = pydantic_model_creator(User, name = "UserIn", exclude_readonly=True, 
exclude=("is_verified", "join_data"))
user_pydanticOut = pydantic_model_creator(User, name= "UserOut", exclude=("password", ))
