from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def hello():
    return {"message": "hello, world!"}


if __name__ == '__main__':
    uvicorn.run("main:app", port=8090, reload=True)
