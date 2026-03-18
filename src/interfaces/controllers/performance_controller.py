from fastapi import APIRouter

router = APIRouter(prefix="/performance",tags=["performance"])

@router.get("/")
async def performance_controller():
    return {"message": "Acá se podria implementar controlador de performance"}