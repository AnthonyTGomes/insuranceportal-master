from pydantic import BaseModel
from datetime import datetime

class HealthRecordRequest(BaseModel):
    condition_id: int
    severity_id: int
    symptoms: str
    treatment: str
    treatment_date: datetime
    veterinarian: str
    remarks: str
    asset_id: int
    by_user_id: int
    current_status_id: int
    start_record : int
    page_size: int
    