from fastapi import FastAPI

import os

app = FastAPI()

@app.get("/health")
async def health_check():
    return  {"status": "UP"}    