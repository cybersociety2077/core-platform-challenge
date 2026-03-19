from fastapi import APIRouter

router = APIRouter(prefix="/data", tags=["data"])


@router.get("/")
async def data():
    return {"message": "Acá se podria implementar controlador de Analytics/Data"}
