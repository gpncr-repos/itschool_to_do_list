from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from routers.crud import router as tasks_router

app = FastAPI()
origins = ["http://localhost:3000"]

@app.get("/")
def say_hello():
    return {"message": "hello, world!"}


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods="*"
)
app.router.include_router(tasks_router)

if __name__ == '__main__':
    uvicorn.run("main:app", port=8090, reload=True)
