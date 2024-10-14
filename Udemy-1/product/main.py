from fastapi import FastAPI
from .import models
from .database import engine
from .routers import product,seller,login



app=FastAPI(
    title="Products API",
    description ="Get details for all the products on our website",
    terms_of_service="http://www.google.com",
    contact={
        "Developer Name":"A S Prajna",
        "Website":"https://asprajna-portfolio.netlify.app",
        "email":"asprajna@gamil.com"
    },
    docs_url="/documentation",
    redoc_url=None
    #license info if needed

)

models.Base.metadata.create_all(engine)



@app.get('/' ,tags=['Home'])
def index():
    return "CRUD with Sqlite"

app.include_router(login.router)
app.include_router(product.router)
app.include_router(seller.router)


