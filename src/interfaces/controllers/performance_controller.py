from fastapi import APIRouter

router = APIRouter(prefix="/performance", tags=["performance"])


@router.get("/")
async def performance():
    return {"message": "Acá se podria implementar controlador de Performance"}
