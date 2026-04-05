from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from app.utils.security import get_password_hash, verify_password, create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES
from app.config.database import user_collection
from app.models.user import UserModel
from datetime import timedelta, datetime, timezone
from app.utils.responses import res_created, res_success_data, res_bad_request

router = APIRouter(prefix="/api/auth", tags=["auth"])

class UserRegisterRequest(BaseModel):
    username: str
    password: str
    
class UserLoginRequest(BaseModel):
    username: str
    password: str

@router.post("/register")
async def register(user: UserRegisterRequest):
    print(user)
    # Check if user already exists
    existing_user = await user_collection.find_one({"username": user.username})
    print(existing_user, "existing_user -----------------------")
    if existing_user:
        return res_bad_request("Username already registered")
        
    # # Hash password and store the base user fields
    hashed_password = get_password_hash(user.password)
    user_dict = {
        "username": user.username,
        "password": hashed_password,
        "profilePicture": None,
        "bio": None,
        "createdAt": datetime.now(timezone.utc).isoformat()
    }
    print(user_dict, "user_dict -----------------------")
    print(hashed_password, "hashed_password -----------------------")
    new_user = await user_collection.insert_one(user_dict)
    
    # # Generate token immediately after registration
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": str(new_user.inserted_id)}, expires_delta=access_token_expires
    )
    return res_created({"access_token": access_token, "token_type": "bearer"})

@router.post("/login")
async def login(user: UserLoginRequest):
    db_user = await user_collection.find_one({"username": user.username})
    if not db_user:
        return res_bad_request("Incorrect username or password")
        
    if not verify_password(user.password, db_user["password"]):
        return res_bad_request("Incorrect username or password")
        
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": str(db_user["_id"])}, expires_delta=access_token_expires
    )
    return res_success_data({"access_token": access_token, "token_type": "bearer"})
