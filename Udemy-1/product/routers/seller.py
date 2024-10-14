from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..import models,schemas
from passlib.context import CryptContext
from product.routers.login import get_current_user


router=APIRouter()

pwd_context=CryptContext(schemes=['bcrypt'],deprecated="auto")


@router.post('/seller',response_model=schemas.DisplaySeller,tags=['Seller'])
def create_seller(request:schemas.Seller,db:Session=Depends(get_db),current_user:schemas.Seller=Depends(get_current_user)):
    hashedpassword=pwd_context.hash(request.password)
    new_seller=models.Seller(username=request.username,email=request.email,password=hashedpassword)
    db.add(new_seller)
    db.commit()
    db.refresh(new_seller)
    return new_seller