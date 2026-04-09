from fastapi import HTTPException
from http import HTTPStatus
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate
from app.models.user import User
from app.core.security import get_password_hash


class UserService:

    def __init__(self,unit_repo : UserRepository):
        self.__unit_repo = unit_repo

    def create(self, data : UserCreate):

        data.password = get_password_hash(data.password)

        user_model = User(**data.model_dump())
        user_exists = self.__unit_repo.get_user_by_email(user_model.email)
        
        if user_exists != None:
            raise HTTPException(status_code=HTTPStatus.CONFLICT , detail= {"mensagem":"usuários existente"})
    
        return self.__unit_repo.create(user_model)
    
     
       
    
    def get_all(self):
        return self.__unit_repo.list()
     

    def get(self, user_id :int):
        if self.__unit_repo.get(user_id) == None:
            raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail= {"mensagem":"usuário não encontrado"})  

        return self.__unit_repo.get(user_id)
           

    def update(self, user_id :int,data : UserCreate):

        user_model  = self.__unit_repo.update(user_id,data)
        if user_model == None:
                raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail= {"mensagem":"usuário não encontrado"})  

        return user_model
            

    def delete(self, user_id :int):

        if  self.__unit_repo.delete(user_id) == False:
            raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail= {"mensagem":"usuário não encontrado"})  
            
        return {"mensagem":"deletado com sucesso"}
                  