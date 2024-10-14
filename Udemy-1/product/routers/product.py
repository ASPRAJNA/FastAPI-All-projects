from fastapi import APIRouter,HTTPException,status,Response
from fastapi.params import Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..import models,schemas
from typing import List
from product.routers.login import get_current_user

router=APIRouter(
    prefix='/product',
    tags=["Products"]
)

@router.post('/',status_code=status.HTTP_201_CREATED,response_model=schemas.DisplayModel)
def add_product(seller_id:int|str,request:schemas.Product,db:Session=Depends(get_db),current_user:schemas.Seller=Depends(get_current_user)):
    new_product=models.Product(name=request.name,description=request.description,price=request.price,seller_id=seller_id)
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

@router.get('/all',response_model=List[schemas.DisplayModel])
def all_product(db:Session=Depends(get_db),current_user:schemas.Seller=Depends(get_current_user)):
    allproducts=db.query(models.Product).all()
    return allproducts

@router.get('/{id}',response_model=schemas.DisplayModel)
def product_by_id(id:int,db:Session=Depends(get_db),current_user:schemas.Seller=Depends(get_current_user)):
    allproducts=db.query(models.Product).filter(models.Product.id==id).first()
    if not allproducts:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="No Products")
    return allproducts

@router.delete('/delete/{id}')
def product_delete(response:Response,id:int,db:Session=Depends(get_db),current_user:schemas.Seller=Depends(get_current_user)):
    deleteprod=db.query(models.Product).filter(models.Product.id==id).delete(synchronize_session=False)
    db.commit()
    if(deleteprod>=1):  
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Product deleted of id:  {id}")
    else:
        return {"Message":f"Product not found with id {id}"}

@router.put('/update/{id}')
def product_update(id:int,request:schemas.Product,db:Session=Depends(get_db),current_user:schemas.Seller=Depends(get_current_user)):
    product=db.query(models.Product).filter(models.Product.id==id)
    if not product.first():
        return {"Message":f"Product not found with id {id}"}
    else:
        product.update(request.dict())
        db.commit()
        return {"Message":f"Product updated Successfully!!"}
