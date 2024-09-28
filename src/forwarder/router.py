from .models import WebhookNotification

from fastapi import APIRouter
import requests
import json

forwarder = APIRouter()


@forwarder.post("/notification")
async def forward(message: WebhookNotification, send_key: str):
    """返回告警信息，可自行挑选信息转发"""
    # 示例代码，可自行在 message 中挑选感兴趣的信息
    interested_data = {
        "receiver": message.receiver,
        "alerts": [{"status": alert.status, "startsAt": alert.startsAt} for alert in message.alerts],
        "version": message.version,
        "externalURL": message.externalURL
    }
    data_str = json.dumps(interested_data, indent=4)

    payload = {
        "title": "grafana 告警",
        "desp": data_str,
        "noip": 1
    }

    url = f"https://sctapi.ftqq.com/{send_key}.send"
    response = requests.post(url, data=payload)
    if response.status_code != 200:
        return {"error": "Request failed", "status_code": response.status_code, "response": response.text}
    try:
        return response.json()  # 尝试解析 JSON
    except json.decoder.JSONDecodeError as e:
        return {"error": "JSON decode error", "message": str(e), "response": response.text}
