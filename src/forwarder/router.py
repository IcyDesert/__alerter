from models import WebhookNotification
from fastapi import APIRouter

forwarder = APIRouter()


@forwarder.post("/notification")
async def forward(message: WebhookNotification):
    """返回告警信息，可自行挑选信息转发"""
    # 示例代码
    interested_data = {
        "receiver": message.receiver,
        "alerts": [{"status": alert.status, "startsAt": alert.startsAt} for alert in message.alerts],
        "version": message.version,
        "externalURL": message.externalURL
    }
    return interested_data
