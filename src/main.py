from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers.crud import router as tasks_router

app = FastAPI()
origins = ["http://localhost:3000"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods="*"
)
app.router.include_router(tasks_router)
