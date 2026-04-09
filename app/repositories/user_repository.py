from sqlmodel import Session, select
from app.models.user import User
from typing import Sequence
from http import HTTPStatus

class UserRepository:
    
    def __init__(self,session : Session ):
        self.__session = session
        

    def create(self,user:User) -> User:
        self.__session.add(user)
        self.__session.commit()
        self.__session.refresh(user)
        return user

    def list(self) -> Sequence[User] :
        return self.__session.exec(select(User)).all() 

    def get(self, id :int )-> (User | None):
        return self.__session.get(User, id)   

    def update(self, id:int ,user:User ):
       
       user_model = self.get(id)
       
       if user_model == None:
          return None   

       user_model.email = user.email
       user_model.name =  user.name
       self.__session.add(user_model)
       self.__session.commit()
       self.__session.refresh(user_model)
       
       return user_model    

    def get_user_by_email(self,email:str):
        return self.__session.exec(select(User).where(User.email == email)).first()

    def delete(self,id :int):
        user_model = self.get(id)
       
        if user_model == None:
            return False     

        self.__session.delete(user_model)
        self.__session.commit()    

        return True