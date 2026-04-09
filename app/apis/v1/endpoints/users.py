
from http import HTTPStatus
from fastapi import APIRouter,Depends,HTTPException
from sqlmodel import Session 
from app.services.user_service import UserService
from app.schemas.user import UserRead,UserCreate
from app.apis.deps import get_user_service

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/",status_code=HTTPStatus.CREATED,response_model=UserRead)
def create_user(data: UserCreate , session : UserService = Depends(get_user_service)):
    return session.create(data)

@router.get("/",status_code=HTTPStatus.OK,response_model=list[UserRead])
def get_list(session : UserService =  Depends(get_user_service)):
    return session.get_all()


@router.get("/{user_id}",status_code=HTTPStatus.OK,response_model=UserRead)
def get_list(user_id : int, session : UserService =  Depends(get_user_service)):
    return session.get(user_id)


@router.put("/{user_id}",status_code=HTTPStatus.OK,response_model=UserRead)
def update_user(user_id : int,data: UserCreate  ,session : UserService =  Depends(get_user_service)):
    return session.update(user_id,data)


@router.delete("/{user_id}",status_code=HTTPStatus.OK)
def get_list(user_id : int, session : UserService =  Depends(get_user_service)):
    session.delete(user_id)
    return {"mensagem":"deletado com sucesso"}