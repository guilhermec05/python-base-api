from fastapi import HTTPException
from http import HTTPStatus
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate
from app.models.user import User

class UserService:

    def __init__(self,unit_repo : UserRepository):
        self.__unit_repo = unit_repo

    def create(self, data : UserCreate):

        try:
            user_model = User(**data.model_dump())
            return self.__unit_repo.create(user_model)
        except Exception as e:
            raise HTTPException(status_code=HTTPStatus.INTERNAL_SERVER_ERROR , detail= {"mensagem":e})  
             
       
    
    def get_all(self):
        try:
            return self.__unit_repo.list()
        except Exception as e:
            raise HTTPException(status_code=HTTPStatus.INTERNAL_SERVER_ERROR , detail= {"mensagem":e})  
     

    def get(self, user_id :int):
        try:    
            if self.__unit_repo.get(user_id) == None:
               raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail= {"mensagem":"usuário não encontrado"})  

            return self.__unit_repo.get(user_id)
        except Exception as e:
            raise HTTPException(status_code=HTTPStatus.INTERNAL_SERVER_ERROR , detail= {"mensagem":e})  
           

    def update(self, user_id :int,data : UserCreate):

        try:
            user_model  = self.__unit_repo.update(user_id,data)
            if user_model == None:
                    raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail= {"mensagem":"usuário não encontrado"})  

            return user_model
        except  Exception as e:
            raise HTTPException(status_code=HTTPStatus.INTERNAL_SERVER_ERROR , detail= {"mensagem":e})  
              

    def delete(self, user_id :int):
        
        try:
            if  self.__unit_repo.delete(user_id) == False:
                    raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail= {"mensagem":"usuário não encontrado"})  
            
        except  Exception as e:
            raise HTTPException(status_code=HTTPStatus.INTERNAL_SERVER_ERROR , detail= {"mensagem":e})  
                  