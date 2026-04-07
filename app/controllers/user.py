# from app.models.user import UserModel
import app.utils.responses as res


async def getUser(user):
    if user and "_id" in user:
        user["_id"] = str(user["_id"])
    return res.res_success_data(user, "User fetched successfully")