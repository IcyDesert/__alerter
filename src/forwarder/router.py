from fastapi import APIRouter
from typing import Dict, Any

forwarder = APIRouter()

@forwarder.post("/notification")
async def forward(message: Dict[str, Any]):
    """返回提供的信息，可以自行进行信息处理"""
    return message