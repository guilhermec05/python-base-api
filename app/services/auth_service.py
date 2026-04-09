from fastapi import HTTPException
from http import HTTPStatus
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserLogin,UserRead
from app.schemas.Token import TokenReponse
from app.core.security import check_password ,create_access_token

class AuthService:

    def __init__(self, user_repo: UserRepository):
        self.__user_repo = user_repo

    def login_for_access(self,login: UserLogin):
        
        user_exists = self.__user_repo.get_user_by_email(login.email)
        
        if user_exists == None or not check_password(login.password, user_exists.password):
            raise HTTPException(
                    status_code=HTTPStatus.UNAUTHORIZED,
                    detail={"mensagem":"usuário ou senha invalidos"}
                )
        
        access_token = create_access_token(data={"name":user_exists.name,"email":user_exists.email,"role":user_exists.role})

        return TokenReponse(token=access_token["token"], expiration=access_token["expiration"])
