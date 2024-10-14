from typing import Optional
from pydantic import BaseModel

class Product(BaseModel):
    name: str
    description:str
    price:float

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "Iphone13",
                    "description": "this is the description of the device",
                    "price":85000,
                }
            ]
        }
    }

class DisplaySeller(BaseModel):
    username:str
    email:str

    class Config:
        orm_mode=True

class DisplayModel(BaseModel):
    name:str
    description:str
    price:float
    seller:DisplaySeller

    class Config:
        orm_mode=True

class Seller(BaseModel):
    username:str
    email:str
    password:str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "username": "user123",
                    "email": "user123@gamil.com",
                    "password": "thisisseceret",
                }
            ]
        }
    }


class Login(BaseModel):
    username:str
    password:str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "username": "user123",
                    "password": "thisisseceret",
                }
            ]
        }
    }

class Token(BaseModel):
    access_token:str
    token_type:str

class TokenData(BaseModel):
    username:Optional[str]=None