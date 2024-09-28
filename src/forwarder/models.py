from typing import Dict, Any, Literal, List, Optional
from pydantic import BaseModel

class Alert(BaseModel):
    """告警信息"""
    status: Literal["firing", "resolved"]
    labels: Dict[str, str]
    annotations: Dict[str, str]
    startsAt: str
    endsAt: str
    generatorURL: str
    fingerprint: str
    silenceURL: str
    values: Dict[str, Any]
    """Will be deprecated soon"""
    # dashboardURL: Optional[HttpUrl]
    # panelURL: Optional[HttpUrl]


class WebhookNotification(BaseModel):
    """告警主体。各参数含义见\n
    https://grafana.com/docs/grafana/latest/alerting/configure-notifications/manage-contact-points/integrations/webhook-notifier/#webhook-fields
    """
    receiver: str
    status: Literal["firing", "resolved"]
    orgId: int
    alerts: List[Alert]
    groupLabels: Optional[dict]
    commonLabels: Dict[str, str]  # 多个告警中的共同标签
    commonAnnotations: Optional[dict]  # 多个告警中的共同注解
    externalURL: str
    version: str
    groupKey: Optional[str]
    truncatedAlerts: int
    """Will be deprecated soon"""
    # title: str
    # state: str
    # message: str
