from sqlmodel import Session
from fastapi import Depends
from app.db.session import get_session
from app.repositories.user_repository import UserRepository
from app.services.user_service import UserService
from app.services.auth_service import AuthService

def get_user_service(session: Session = Depends(get_session) ) -> UserService:
    repo = UserRepository(session)
    return UserService(repo)

def get_auth_service(session: Session = Depends(get_session)) -> AuthService:
    repo = UserRepository(session)
    return AuthService(repo)
