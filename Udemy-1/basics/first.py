from fastapi import FastAPI

app=FastAPI()


@app.get('/')
def welcome():
    return 'Welcome to FastAPI wordld'


@app.get('/home')
def index():
    return 'Hello FastAPI!!'

#handling another path
@app.get('/property')
def property():
    return 'This is the property page'

#Returning JSON instead of simple string
@app.get('/movies')
def movies():
    return {'movie list':{'movie 1','movie 2','movie 3'}}

"""
@app.get('/property/1')
def property1():
    return 'This is the property page for property1'


Path Parameters
parametes included in path of url and used inside the functions

@app.get('/property/{id}')
def property_id(id):
    return f'This is property for {id}'
--------------------------------------------
Path parameter with type


"""

@app.get('/property/{id}')
def property_id(id:int):
    return f'This is property for {id}'

@app.get('/profile/{username}')
def profile(username:str):
    return {f'This is aprofile page for : {username}'}

#Ordering of routes place dynamic routes after static

@app.get('/user/admin')
def admin():
    return{f'This is ADMIN'}

@app.get('/user/{username}')
def profile_page(username:str):
    return{f'this is a profile of {username}'}

"""

#Query Parameters

#http://127.0.0.1:8000/products?id=2
@app.get('/products')
def query_param(id):
    return {f'Procuct with id :{id}'}

#multple query param
#url : http://127.0.0.1:8000/productsprice?id=2&price=100
@app.get('/productsprice')
def query_param2(id,price):
    return {f'Procuct with id :{id} and price is {price}'}

#Optional /Default Values
@app.get('/productsprice')
def query_param2(id=0,price=100):
    return {f'Procuct with id :{id} and price is {price}'}

#Default with datattypes
@app.get('/productsprice')
def query_param2(id:int=1,price:int=100):
    return {f'Procuct with id :{id} and price is {price}'}

@app.get('/profile/{userid}/comments')
def profile_comments(commentid:int=10,userid:int=1):
    return {f'Profile page with user :{userid} and commentid {commentid}'}

#Query and path parameter
@app.get('/profile/{userid}/comments')
def profile_comments(commentid:int=10,userid:int=1):
    return {f'Profile page with user :{userid} and commentid {commentid}'}

"""



#Url http://127.0.0.1:8000/profile/10/comments?commentid=100

@app.get('/productsprice')
def query_param2(id:int,price=None):
    return {f'Procuct with id :{id} and price is {price}'}
