from sqlmodel import Session
from fastapi import Depends
from app.db.session import get_session
from app.repositories.user_repository import UserRepository
from app.services.user_service import UserService

def get_user_service(session: Session = Depends(get_session) ) -> UserService:
    repo = UserRepository(session)
    return UserService(repo)

