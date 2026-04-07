# from app.models.user import UserModel
import app.utils.responses as res
import app.services.user as userService


async def getUser(user):
    try:
        if user and "_id" in user:
            user["_id"] = str(user["_id"])
        return res.res_success_data(user, "User fetched successfully")
    except Exception as e:
        return res.res_error(str(e))


async def updateUser(user, body):
    try:
        return await userService.updateUser(user, body)
    except Exception as e:
        return res.res_error(str(e))
