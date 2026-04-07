from app.utils.security import (
    get_password_hash,
    verify_password,
    create_access_token,
    ACCESS_TOKEN_EXPIRE_MINUTES,
)
from app.config.database import user_collection
from datetime import timedelta, datetime, timezone
from app.utils.responses import res_bad_request, res_created, res_success_data
from app.utils.cloudinary import uploadImages


async def registerService(user):
    # Check if user already exists
    existing_user = await user_collection.find_one({"username": user["username"]})
    if existing_user:
        return res_bad_request("Username already registered")

    # Hash password and store the base user fields
    hashed_password = get_password_hash(user["password"])
    user_dict = {
        "username": user["username"],
        "password": hashed_password,
        "bio": user["bio"] or None,
        "createdAt": datetime.now(timezone.utc).isoformat(),
    }

    new_user = await user_collection.insert_one(user_dict)
    if new_user:
        image_url = await uploadImages(user["profilePicture"])
        await user_collection.update_one(
            {"_id": new_user.inserted_id}, {"$set": {"profilePicture": image_url}}
        )

    # Generate token immediately after registration
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": str(new_user.inserted_id)}, expires_delta=access_token_expires
    )

    # Clean up user_dict for the response
    user_dict["profilePicture"] = image_url
    user_dict["_id"] = str(user_dict["_id"])  # stringify the ObjectId added by motor
    user_dict.pop("password", None)  # Remove sensitive password hash

    return res_created(
        {
            "user": user_dict,
            "access_token": access_token,
        }
    )


async def loginService(user):
    db_user = await user_collection.find_one(
        {"username": user.username},
    )
    if not db_user:
        return res_bad_request("Incorrect username or password")

    if not verify_password(user.password, db_user["password"]):
        return res_bad_request("Incorrect username or password")

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": str(db_user["_id"])}, expires_delta=access_token_expires
    )
    db_user.pop("password", None)  # Remove sensitive password hash
    db_user["_id"] = str(db_user["_id"])  # stringify the ObjectId added by motor
    return res_success_data(
        {"user": db_user, "access_token": access_token, "token_type": "bearer"}
    )
