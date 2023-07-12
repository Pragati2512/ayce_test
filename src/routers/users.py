from fastapi import APIRouter, status, Request, Header, Depends, BackgroundTasks
from src.pydentics.user_schemas import Login_Fields, UserCreate
from src.functions.user import UserActivity

user_router = APIRouter(
    prefix='/user',
    tags=['Manage User']
)
user_data = UserActivity()


@user_router.post("/auth/", status_code=status.HTTP_200_OK)
async def authenticate(request: Request, credentials: Login_Fields):
    """User authentication"""

    return user_data.user_auth(request, credentials)


@user_router.post("/register/", status_code=status.HTTP_200_OK)
async def register(request: Request, credentials: UserCreate):
    """User registration"""

    return user_data.user_register(request, credentials)
