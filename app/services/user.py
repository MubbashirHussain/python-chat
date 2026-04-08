from app.config.database import user_collection
import app.utils.responses as res
from bson import ObjectId
from app.utils.cloudinary import uploadImages


async def getUser(user):
    try:
        if user and "_id" in user:
            user["_id"] = str(user["_id"])
        return res.res_success_data(user, "User fetched successfully")
    except Exception as e:
        return res.res_error(str(e))


async def updateUser(user, body):
    if user and "_id" in user:
        try:
            if body["profilePicture"]:
                profilePicture = await uploadImages(body["profilePicture"])

            result = await user_collection.update_one(
                {"_id": ObjectId(user["_id"])},
                {
                    "$set": {
                        "username": body["username"],
                        "name": body["name"],
                        "profilePicture": profilePicture,
                        "bio": body["bio"],
                    }
                },
            )
            if not result.acknowledged:
                return res.res_error("User not updated")

        except Exception as e:
            return res.res_error(str(e))

    # if user["password"]:
    #     del user["password"]
    user["_id"] = str(user["_id"])
    return res.res_success_data(user, "User updated successfully")


async def deleteUser(user):
    try:
        result = await user_collection.update_one(
            {"_id": ObjectId(user["_id"])}, {"$set": {"isDeleted": True}}
        )
        if not result.acknowledged:
            return res.res_error("User not deleted")
    except Exception as e:
        return res.res_error(str(e))
    return res.res_success("User deleted successfully")
