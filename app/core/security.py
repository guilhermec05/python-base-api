from fastapi import Depends,HTTPException
from http import HTTPStatus
from jwt import encode,decode
from zoneinfo import ZoneInfo
from app.core.config import settings
from datetime import datetime,timedelta
from pwdlib import PasswordHash
from fastapi.security import OAuth2PasswordBearer


pwd_context = PasswordHash.recommended()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def create_access_token(data :dict):
    to_encode  = data.copy()
    expiration = datetime.now(tz=ZoneInfo("UTC")) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expiration})
    token = encode(to_encode,settings.SECRET_KEY,algorithm=settings.ALGORITHM)
    return {"token": token ,"expiration":expiration.strftime("%Y-%m-%d %H:%M:%S"),"role":to_encode['role']}

def get_current_user(token : str = Depends(oauth2_scheme) ):
    try:
        payload = decode(token,settings.SECRET_KEY,algorithms=[settings.ALGORITHM])
        subject_email = payload.get('email')
        if not subject_email:
            raise HTTPException(status_code=HTTPStatus.UNAUTHORIZED, detail={"mensagem":"email invalido"})
        return {
            "email":payload.get('email'),
            "role":payload.get('role')
        } 
    except Exception as e:
        raise HTTPException(status_code=HTTPStatus.UNAUTHORIZED, detail=str(e))

    

def permission_router(roles:list[str]):

    def role_check(user = Depends(get_current_user)):
        if user["role"] not in roles or user["role"]  == 'A':
            raise HTTPException(status_code=HTTPStatus.FORBIDDEN, detail={"mensagem":"você não tem permissão de acesso"})   

        return user 
      
    return  role_check   
def get_password_hash(password : str):
    return pwd_context.hash(password)

def check_password(password:str, hash_password:str):
    return pwd_context.verify(password,hash=hash_password)