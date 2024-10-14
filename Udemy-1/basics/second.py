from fastapi import FastAPI,Form
from pydantic import BaseModel,Field,HttpUrl
from typing import List,Set
from uuid import UUID
from datetime import date,datetime,time,timedelta


second=FastAPI()

class Profile(BaseModel):
    name:str
    email:str
    age:int

class Image(BaseModel):
    url:HttpUrl
    name:str

#Form pip install python-multipart
@second.post('/login')
def login(username:str=Form(...),password:str=Form(...)):
    return {"user":username}

#Nesting Python Datatypes in model
#nesting pydantic model
class Product(BaseModel):
    name:str
    price:int =Field(title="Price of the item",description="price of item of the sale",gt=100)
    discount:int
    discounted_price:float
    tags:Set[str]=[]
    image:list[Image]

    model_config={
        "json_schema_extra": {
        "example":{
            "name":"Phone",
            "price":100,
            "discount":0,
            "discounted_price":0,
            "tags":["Electronics","Computers","Devices"],
            "image":[
                {
                    "url":"http://www.iphone.png",
                    "name":"PhoneImage"
                },
                {
                    "url":"http://www.iphone.png",
                    "name":"PhoneImage"
                }
                ]
        }
        }
        }
        

#Deeply nested model
class Offer(BaseModel):
    name:str=Field(examples=["Big biliion sale","Diwali offer "])
    dicount:float
    price:float
    products:List[Product]

class User(BaseModel):
    name :str
    email:str

@second.get('/')
def welcome():
    return 'Welcome to FastAPI wordld-2'

"""
Request Body and Response body and Request URL
@second.post('/adduser')
def adduser(profile:Profile):
    return profile.name

@second.post('/addproduct')
def addprod(product:Product):
    product.discounted_price=product.price-(product.price*product.discount)/100
    return product

#passing path and query parameter to request

"""

@second.post('/adduser')
def adduser(profile:Profile):
    return profile.name
    
#passing path and query parameter to request
@second.post('/addproduct/{prod_id}')
def addprod(product:Product,prod_id:int,category:str):
    product.discounted_price=product.price-(product.price*product.discount)/100
    return {"product_id":prod_id,"product":product,"category":category}


#multiple modles to same route
@second.post('/purchase/')
def purchase(user:User,product:Product):
    return {"user":user,"product":product}


#defining body fileds for metadata
# price:int =Field(title="Price of the item",description="price of item of the sale",gt=100)
  
#riute for deeply nested model
@second.post('/offer')
def add_offer(offer:Offer):
    return  offer



"""

"""

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "Foo",
                    "description": "A very nice Item",
                    "price": 35.4,
                    "tax": 3.2,
                }
            ]
        }
    }


@second.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results

#time datatype
class Event(BaseModel):
    event_id:UUID
    start_date:date
    start_time:datetime
    end_time:datetime
    repeat_time:time
    completion_time:timedelta

@second.post('/addevent')
def events(event:Event):
    return event

#Form to submit data
