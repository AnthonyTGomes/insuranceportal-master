from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel, Field


class FarmersInfoRequest(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    asset_status_id: Optional[int] = None
    start_record : Optional[int] = None
    page_size: Optional[int] = None
    by_user_id: int = Field(..., description="Auto-injected from request.user.id")


class InsuranceApplicationRequest(BaseModel):
    id: int = None
    insurance_number: str = None
    sum_insured: float = None
    premium_amount: Optional[float] = None
    insurance_start_date: Optional[date] = None
    insurance_end_date: Optional[date] = None
    insurance_status: str = None
    policy_terms: Optional[str] = None
    insurance_certificate: Optional[str] = None
    insurance_agent: Optional[str] = None
    renewal_reminder_sent: bool = None
    created_at: datetime = None
    updated_at: datetime = None
    remarks: Optional[str] = None
    asset_id: int = None
    created_by_id: Optional[int] = None
    updated_by_id: Optional[int] = None
    insurance_provider_id: Optional[int] = None
    is_claimed: bool = None
    insurance_product_id: int = None
    view_count: int = None
    start_record : Optional[int] = None
    page_size: Optional[int] = None    
    by_user_id: int = Field(..., description="Auto-injected from request.user.id")


class InsuranceProductRequest(BaseModel):
    id: int = None
    premium_percentage: float = None
    insurance_period_id: int = None
    insurance_type_id: int = None
    insurance_category_id: int = None
    insurance_company_id: int = None
    start_record : Optional[int] = None
    page_size: Optional[int] = None   
    by_user_id: int = Field(..., description="Auto-injected from request.user.id")        