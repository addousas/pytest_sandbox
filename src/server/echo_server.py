
from fastapi import FastAPI

app = FastAPI()

@app.get("/echo/{message}")
def echo_message(message: str):
    return {"message": message}



