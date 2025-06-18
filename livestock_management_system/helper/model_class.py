from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class HealthRecordRequest(BaseModel):
    condition_id: Optional[int] = None
    severity_id: Optional[int] = None
    symptoms: Optional[str] = None
    treatment: Optional[str] = None
    treatment_date: Optional[datetime] = None
    veterinarian: Optional[str] = None
    remarks: Optional[str] = None
    asset_id: Optional[int] = None
    by_user_id: Optional[int] = None
    current_status_id: Optional[int] = None
    start_record : Optional[int] = None
    page_size: Optional[int] = None

class VaccineRequest(BaseModel):
    id: Optional[int] = None 
    name: Optional[str] = None
    remarks: Optional[str] = None
    start_record : Optional[int] = None
    page_size: Optional[int] = None


class VaccinationScheduleRequest(BaseModel):
    id: Optional[int] = None
    asset_id: Optional[int] = None
    vaccine_id: Optional[int] = None
    due_date: Optional[datetime] = None
    is_completed: Optional[bool] = None
    completed_at: Optional[datetime] = None
    remarks: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    is_active: Optional[bool] = None
    created_by: Optional[int] = None
    modified_by: Optional[int] = None           
    start_record : Optional[int] = None
    page_size: Optional[int] = None


class AssetMedicalConditionRequest(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    start_record : Optional[int] = None
    page_size: Optional[int] = None

class AssetMedicalConditionSeverityRequest(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    start_record : Optional[int] = None
    page_size: Optional[int] = None

class IncomeExpenseRequest(BaseModel):
    ledger_id: Optional[int] = None
    amount: Optional[int] = None
    txn_date: Optional[datetime] = None
    description: Optional[str] = None
    organization_id: Optional[int] = None
    branch_id: Optional[int] = None
    created_by: Optional[int] = None
    start_record : Optional[int] = None
    page_size: Optional[int] = None

class AssetInfoRequest(BaseModel):
    start_record : Optional[int] = None
    page_size: Optional[int] = None

class GlsLedgersRequest(BaseModel):
    ledger_id: int = None
    code: Optional[str] = None
    name_ledger: Optional[str] = None
    name_ledger_bangla: Optional[str] = None
    type: Optional[str] = None
    is_control_item: Optional[bool] = None
    is_cost_revinue_center: Optional[bool] = None
    is_product_line: Optional[bool] = None
    is_vendor: Optional[bool] = None
    is_customer: Optional[bool] = None
    sort: Optional[int] = None
    created_at: Optional[datetime] = None
    modified_at: Optional[datetime] = None
    gls_organization_id: Optional[int] = None
    is_cash: Optional[bool] = None
    is_bank: Optional[bool] = None
    is_petty_cash: Optional[bool] = None
    is_petty_cash_expense: Optional[bool] = None
    is_ie_account: Optional[bool] = None
    is_bank_investment: Optional[bool] = None
    created_by: Optional[int] = None
    modified_by: Optional[int] = None
    ledger_activity: Optional[str] = None

'''
 # @ Author: Tanmay Anthony Gomes
 # @ Create Time: 2025-06-12 15:13:41
 # @ Modified by: Tanmay Anthony Gomes
 # @ Modified time: 2025-06-12 17:49:03
 # @ Description: response function for returning result. will be called from DAL classes
 '''
def _response(status, message, data=None):
    return {
        "status": status,
        "message": message,
        "data": data or []
    }
