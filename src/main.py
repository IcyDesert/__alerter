from fastapi import FastAPI
from src.forwarder import router

app = FastAPI()
app.include_router(router.forwarder)

@app.get("/")
async def root():
    """测试代码"""
    return {"message": "Hello alerter!"}