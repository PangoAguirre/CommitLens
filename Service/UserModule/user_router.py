from fastapi import APIRouter, Depends
from Service.UserModule.dtos import LoginDTO
from dependencies import get_user_repository

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/login")
def login(credentials: LoginDTO, user_service = Depends(get_user_repository)):
    return user_service.login(credentials.username, credentials.password)