from typing import List
from fastapi import APIRouter, Depends, Form, HTTPException, FastAPI
from src.DTO.User import User
from src.Security import CreateTokenJWT, GetPasswordHash, IsPassword

router = FastAPI()

@router.post("/login")
async def login(username: str = Form(...), password: str = Form(...)):
    user = await User.objects.get_or_none(email=username)
    if not user or not IsPassword(password, user.hash_password):
        raise HTTPException(status_code=403,
                            detail="Email ou nome de usuário incorretos"
                           )
    return {
        "access_token": CreateTokenJWT(user.id),
        "token_type": "bearer",
    }