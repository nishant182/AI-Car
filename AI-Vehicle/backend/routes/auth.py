from fastapi import APIRouter
from services.security import create_access_token
from schemas.auth import RegisterRequest, LoginRequest

router = APIRouter()


@router.post("/register")
def register(user: RegisterRequest):
    return {
        "message": "User registered successfully",
        "user": user.model_dump()
    }

@router.post("/login")
def login(user: LoginRequest):

    token = create_access_token({
        "email": user.email
    })

    return {
        "message": "Login successful",
        "access_token": token,
        "token_type": "bearer",
        "email": user.email
    }