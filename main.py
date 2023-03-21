from fastapi import FastAPI
from tortoise import models 
from tortoise.contrib.fastapi import register_tortoise
from models import * 
from authentication import (get_hashed_password)

#signals

from tortoise.signals import post_save
from typing import List, Optional, Type
from tortoise import BaseDBAsyncClient

app = FastAPI()

@post_save(User)       


@app.post("/daftar")
async def user_registration(user: user_pydanticIn):
    user_info = user.dict(exclude_unset=True)
    user_info["password"] = get_hashed_password(user_info["password"])
    user_obj = await User.create(**user_info)
    new_user = await user_pydantic.from_tortoise_orm(user_obj)
    return{
        "status": "ok",
        "data" : "Hello thanks for choosing our service"
    }


@app.post("/tabung")
@app.post("/tarik")
@app.post("/salod/{no_rekening}")

@app.get("/")
def index():
    return {"Message": "Hello World"}

register_tortoise(
    app,
    db_url="sqlite://database.sqlite3",
    modules={"models": ["models"]},
    generate_schemas=True,
    add_exception_handlers=True
)