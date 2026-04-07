from app.utils.responses import res_created, res_success_data, res_bad_request
from app.services.auth import registerService, loginService


async def registerController(user):
    result = await registerService(user)
    return result


async def loginController(user):
    result = await loginService(user)
    return result
