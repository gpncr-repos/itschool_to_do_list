from fastapi import FastAPI
from routers.crud import router as tasks_router

app = FastAPI()
app.router.include_router(tasks_router)
