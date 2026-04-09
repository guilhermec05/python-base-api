from fastapi import APIRouter,Depends
from http import HTTPStatus
from app.schemas.Token import TokenReponse
from app.schemas.user import UserLogin
from app.services.auth_service import AuthService 
from app.apis.deps import get_auth_service
from app.apis.v1.endpoints.base_endpoint import result 


router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/token",status_code=HTTPStatus.OK,response_model=TokenReponse)
def create_user(
    body_login: UserLogin,
    session : AuthService =  Depends(get_auth_service)
):
  return result(session.login_for_access(body_login))  
 

