from typing import Optional
from pydantic import BaseModel

# Model Class for SMS request
class SendSMSRequest(BaseModel):
    msisdn: Optional[str] = None
    message: Optional[int] = None
    clienttransid: Optional[str] = None
