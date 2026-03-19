from fastapi import FastAPI
from src.interfaces.controllers import security_controller
from src.interfaces.controllers import performance_controller
from src.interfaces.controllers import automation_controller
from src.interfaces.controllers import data_controller

app = FastAPI()

app.include_router(security_controller.router)
app.include_router(performance_controller.router)
app.include_router(automation_controller.router)
app.include_router(data_controller.router)
