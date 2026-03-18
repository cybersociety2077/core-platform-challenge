from fastapi import APIRouter

router = APIRouter(prefix="/automation", tags=["automation"])


@router.get("/")
async def automation():
    return {"message": "Acá se podria implementar controlador de Automation"}
