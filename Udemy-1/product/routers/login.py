from fastapi import APIRouter,HTTPException,status,Depends
from ..import schemas,database,models
from ..database import get_db
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from datetime import datetime,timedelta
from jose import jwt,JWTError
from fastapi.security import OAuth2PasswordBearer
from fastapi.security.oauth2 import OAuth2PasswordRequestForm

secret_key='yty7LQwChkyU4Ny8C1Q5zPJPfRkuk5pUk8vyJJRyR3s='
algorithm="HS256"
access_token_exp_min=20


pwd_context=CryptContext(schemes=['bcrypt'],deprecated="auto")
oauth2_scheme=OAuth2PasswordBearer(tokenUrl="login")


def generate_access_token(data:dict):
    to_encode=data.copy()
    expire=datetime.utcnow()+timedelta(minutes=access_token_exp_min)
    to_encode.update({"exp":expire})
    encoded_jwt=jwt.encode(to_encode,secret_key,algorithm=algorithm)
    return encoded_jwt


router=APIRouter(
   tags=["Login"] 
)

@router.post('/login')
def login(request:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(get_db)):
    seller=db.query(models.Seller).filter(models.Seller.username==request.username).first()
    if not seller :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Username not found")
    if not pwd_context.verify(request.password,seller.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Invalid password")
    #Gen JWT token
    access_token=generate_access_token(data={"sub":seller.username})
    return {"access_token":access_token,"token_type":"bearer"}

def get_current_user(token:str=Depends(oauth2_scheme)):
    cred_exception=HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid auth credentials",
                headers={'WWW-Authenticaticate':'Bearer'})
    try:
        payload=jwt.decode(token,secret_key,algorithms=[algorithm])
        username:str= payload.get('sub')
        if username is None:
            raise cred_exception
        token_data=schemas.TokenData(username=username)
    except JWTError:
        raise cred_exception