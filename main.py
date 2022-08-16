from fastapi import FastAPI, status

app = FastAPI()
#

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/healthcheck")
async def check():
    return status.HTTP_200_OK
