# from app.models.user import UserModel
import app.utils.responses as res
import app.services.user as userService


async def getUser(user):
    try:
        return await userService.getUser(user)
    except Exception as e:
        return res.res_error(str(e))


async def updateUser(user, body):
    try:
        return await userService.updateUser(user, body)
    except Exception as e:
        return res.res_error(str(e))
