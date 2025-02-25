from urllib.request import Request
from starlette.responses import JSONResponse


async def app_id_middleware(request: Request, call_next):
    app_id = request.headers.get("appid")

    if not app_id:
        return JSONResponse(
            status_code=400,
            content={"error": "Header appId es requerido bro"}
        )

    if not app_id.isdigit():
        return JSONResponse(
            status_code=400,
            content={"error": "appId debe ser un número válido"}
        )

    response = await call_next(request)
    return response

