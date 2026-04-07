from typing import Any, Optional
from fastapi.responses import JSONResponse


def _write_response(status_code: int, msg: Any) -> JSONResponse:
    return JSONResponse(
        status_code=status_code,
        content={"status": True, "code": status_code, "message": msg},
    )


def _write_response_data(status_code: int, msg: str, data: Any) -> JSONResponse:
    return JSONResponse(
        status_code=status_code,
        content={"status": True, "code": status_code, "message": msg, "data": data},
    )


def _write_response_error(status_code: int, msg: str, err: Any) -> JSONResponse:
    return JSONResponse(
        status_code=status_code,
        content={"status": False, "code": status_code, "message": msg, "error": err},
    )


def res_success(msg: str = "Success") -> JSONResponse:
    return _write_response(200, msg)


def res_success_data(data: Any, msg: str = "Success") -> JSONResponse:
    return _write_response_data(200, msg, data)


def res_created(data: Any, msg: str = "Created") -> JSONResponse:
    return _write_response_data(201, msg, data)


def res_updated(data: Any, msg: str = "Updated") -> JSONResponse:
    return _write_response_data(200, msg, data)


def res_bad_request(err: Any = "Bad Request") -> JSONResponse:
    return _write_response_error(400, "Bad Request", err)


def res_internal_error(err: Any = "Internal Server Error") -> JSONResponse:
    print("<<<<===== ** SERVER ERROR START ** =====>>>>")
    print(err)
    print("<<<<===== ** SERVER ERROR END ** =====>>>>")
    return _write_response_error(500, "Internal Server Error", err)


def res_not_found(err: Any = "Not Found") -> JSONResponse:
    return _write_response_error(404, "Not Found", err)


def res_unauthorized(err: Any = "Unauthorized") -> JSONResponse:
    return _write_response_error(401, "Unauthorized", err)


def res_authenticate(err: Any = "Unauthorized") -> JSONResponse:
    response = _write_response_error(401, "Unauthorized", err)
    response.headers["WWW-Authenticate"] = 'Basic realm="Authorization Required"'
    return response


def socket_console(data: Any) -> None:
    print("<<<<===== ** SOCKET CONSOLE START ** =====>>>>")
    print(data)
    print("<<<<===== ** SOCKET CONSOLE END ** =====>>>>")


def basic_controller_res(result: Optional[dict] = None) -> JSONResponse:
    if not result:
        return res_not_found("Not Found")

    if "error" in result:
        error_info = result["error"]
        if getattr(error_info, "status", None) == 401 or (
            isinstance(error_info, dict) and error_info.get("status") == 401
        ):
            return res_unauthorized(result["error"])
        return res_bad_request(result["error"])

    if "success" in result:
        success_info = result["success"]
        status_code = getattr(success_info, "status", None)
        if isinstance(success_info, dict):
            status_code = success_info.get("status")
            data = success_info.get("data")
            msg = success_info.get("message", "")
        else:
            data = getattr(success_info, "data", None)
            msg = getattr(success_info, "message", "")

        if status_code == 201:
            return res_created(data if data is not None else success_info)
        if data is not None:
            return res_success_data(data)
        return res_success(msg)

    return res_internal_error("Invalid result format")


def res_error(err: Any = "Internal Server Error") -> JSONResponse:
    return _write_response_error(500, "Internal Server Error", err)
