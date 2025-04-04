from pydantic import BaseModel

from libertai_utils.interfaces.subscription import SubscriptionAccount


class BaseDeleteAgentBody(BaseModel):
    subscription_id: str
    password: str


class BaseSetupAgentBody(BaseDeleteAgentBody):
    account: SubscriptionAccount


class UpdateAgentResponse(BaseModel):
    instance_ip: str
    error_log: str
