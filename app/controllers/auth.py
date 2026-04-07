import app.utils.responses as res
from app.services.auth import registerService, loginService


async def registerController(user):
    try:
        result = await registerService(user)
        return result
    except Exception as e:
        return res.res_error(str(e))


async def loginController(user):
    try:
        result = await loginService(user)
        return result
    except Exception as e:
        return res.res_error(str(e))
