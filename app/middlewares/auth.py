from fastapi import Request, HTTPException, status, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.utils.security import SECRET_KEY, ALGORITHM
from app.config.database import user_collection
import jwt
from bson import ObjectId

# This dependency automatically checks for the Authorization Bearer header
security = HTTPBearer()


async def verifyToken(
    credentials: HTTPAuthorizationCredentials = Depends(security),
):
    token = credentials.credentials
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        # Decode the JWT token
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise credentials_exception
    except jwt.PyJWTError:
        raise credentials_exception

    # Find the user by ID in MongoDB
    try:
        user = await user_collection.find_one(
            {"_id": ObjectId(user_id), "isDeleted": False}, {"password": 0}
        )
        if user is None:
            raise credentials_exception
    except Exception:
        raise credentials_exception

    return user
