from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from core.security import hash_password, verify_password, create_access_token

router = APIRouter(prefix="/auth", tags=["Auth"])

# Dummy in-memory user store (prod me DB use karo)
fake_users_db = {
    "yash": {"username": "yash", "hashed_password": hash_password("1234"), "scopes": ["user"]},
    "admin": {"username": "admin", "hashed_password": hash_password("admin123"), "scopes": ["admin"]},
}

class LoginRequest(BaseModel):
    username: str
    password: str

@router.post("/signup")
async def signup(user: LoginRequest):
    if user.username in fake_users_db:
        raise HTTPException(status_code=400, detail="User already exists")
    fake_users_db[user.username] = {
        "username": user.username,
        "hashed_password": hash_password(user.password),
        "scopes": ["user"]
    }
    return {"msg": "User created successfully"}

@router.post("/token")
async def login(data: LoginRequest):
    user = fake_users_db.get(data.username)
    if not user or not verify_password(data.password, user["hashed_password"]):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    # create JWT with scopes
    access_token = create_access_token(subject=user["username"], scopes=user["scopes"])
    return {"access_token": access_token, "token_type": "bearer"}
from fastapi import APIRouter, Security
from core.security import get_current_user

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/me")
async def get_profile(user=Security(get_current_user, scopes=["user"])):
    return {"msg": "Profile info", "username": user["username"], "scopes": user["scopes"]}

@router.get("/admin")
async def admin_area(user=Security(get_current_user, scopes=["admin"])):
    return {"msg": f"Welcome {user['username']}!", "role": "Admin"}