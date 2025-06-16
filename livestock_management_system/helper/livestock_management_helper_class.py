# user_management_system/helper/user_management_helper_class.py
import psycopg2
from django.conf import settings
import json
from db import get_db_connection, call_db_function
from livestock_management_system.helper.model_class import AssetMedicalConditionRequest, AssetMedicalConditionSeverityRequest, HealthRecordRequest, IncomeExpenseRequest, VaccinationScheduleRequest, _response, VaccineRequest

'''
 # @ Author: Tanmay Anthony Gomes
 # @ Create Time: 2025-06-11 15:01:24
 # @ Modified by: Tanmay Anthony Gomes
 # @ Modified time: 2025-06-11 15:58:18
 # @ Description: Function for getting asset list from DB
'''
def get_assets_list(start_record: int, page_size: int):
    try:
        with get_db_connection() as conn: # calling get_db_connection for getting the connection string
            rows = call_db_function(conn, "public.fn_get_assets_list", (start_record, page_size)) # calling fn_get_assets_list function from DB  to get data.

            if not rows:
                return _response("failed", "Error Occured While Processing Request")

            result = rows[0]  
            data = result["data"]
            if isinstance(data, str):
                data = json.loads(data)

            return _response(result["status"], result["message"], data)

    except Exception as ex:
        return _response("error", str(ex))

'''
 # @ Author: Tanmay Anthony Gomes
 # @ Create Time: 2025-06-12 12:44:24
 # @ Modified by: Tanmay Anthony Gomes
 # @ Modified time: 
 # @ Description: Function For Inserting Livestock Health records 
 '''
def add_assets_health_record(record: HealthRecordRequest):
    try:
        with get_db_connection() as conn: # calling get_db_connection for getting the connection string
            rows = call_db_function(conn, "public.fn_insert_assets_health_records_v2", [record.json()]) # calling fn_get_assets_list function from DB  to get data.

            if not rows:
                return _response("failed", "Error Occured While Processing Request")

            result = rows[0]  
            data = result["data"]
            if isinstance(data, str):
                data = json.loads(data)

            return _response(result["status"], result["message"], data)

    except Exception as ex:
        return _response("error", str(ex))

'''
 # @ Author: Tanmay Anthony Gomes
 # @ Create Time: 2025-06-11 15:01:24
 # @ Modified by: Tanmay Anthony Gomes
 # @ Modified time: 2025-06-12 17:44:57
 # @ Description: To get Live stock's health records
 '''
def get_assets_health_record(record: HealthRecordRequest):
    try:
        with get_db_connection() as conn: # calling get_db_connection for getting the connection string
            rows = call_db_function(conn, "public.fn_get_assets_health_record_list", [record.json()]) # calling fn_get_assets_list function from DB  to get data.

            if not rows:
                return _response("failed", "Error Occured While Processing Request")

            result = rows[0]  
            data = result["data"]
            if isinstance(data, str):
                data = json.loads(data)

            return _response(result["status"], result["message"], data)

    except Exception as ex:
        return _response("error", str(ex))


def get_asset_vaccine_list(record: VaccineRequest):
    try:
        with get_db_connection() as conn: # calling get_db_connection for getting the connection string
            rows = call_db_function(conn, "public.fn_get_asset_vaccine", [record.json()]) # calling fn_get_assets_list function from DB  to get data.

            if not rows:
                return _response("failed", "Error Occured While Processing Request")

            result = rows[0]  
            data = result["data"]
            if isinstance(data, str):
                data = json.loads(data)

            return _response(result["status"], result["message"], data)

    except Exception as ex:
        return _response("error", str(ex))
    
def add_asset_vaccination_schedule(record: VaccinationScheduleRequest):
    try:
        with get_db_connection() as conn: # calling get_db_connection for getting the connection string
            rows = call_db_function(conn, "public.fn_insert_assets_vaccination_schedule", [record.json()]) # calling fn_get_assets_list function from DB  to get data.

            if not rows:
                return _response("failed", "Error Occured While Processing Request")

            result = rows[0]  
            data = result["data"]
            if isinstance(data, str):
                data = json.loads(data)

            return _response(result["status"], result["message"], data)

    except Exception as ex:
        return _response("error", str(ex))


def get_asset_vaccination_schedule(record: VaccinationScheduleRequest):
    try:
        with get_db_connection() as conn: # calling get_db_connection for getting the connection string
            rows = call_db_function(conn, "public.fn_get_asset_vaccination_schedule", [record.json()]) # calling fn_get_assets_list function from DB  to get data.

            if not rows:
                return _response("failed", "Error Occured While Processing Request")

            result = rows[0]  
            data = result["data"]
            if isinstance(data, str):
                data = json.loads(data)

            return _response(result["status"], result["message"], data)

    except Exception as ex:
        return _response("error", str(ex))




def get_asset_medical_condition(record: AssetMedicalConditionRequest):
    try:
        with get_db_connection() as conn: # calling get_db_connection for getting the connection string
            rows = call_db_function(conn, "public.fn_get_asset_medical_condition", [record.json()]) # calling fn_get_assets_list function from DB  to get data.

            if not rows:
                return _response("failed", "Error Occured While Processing Request")

            result = rows[0]  
            data = result["data"]
            if isinstance(data, str):
                data = json.loads(data)

            return _response(result["status"], result["message"], data)

    except Exception as ex:
        return _response("error", str(ex))

def get_asset_medical_condition_severity(record: AssetMedicalConditionSeverityRequest):
    try:
        with get_db_connection() as conn: # calling get_db_connection for getting the connection string
            rows = call_db_function(conn, "public.fn_get_asset_medical_condition_severity", [record.json()]) # calling fn_get_assets_list function from DB  to get data.

            if not rows:
                return _response("failed", "Error Occured While Processing Request")

            result = rows[0]  
            data = result["data"]
            if isinstance(data, str):
                data = json.loads(data)

            return _response(result["status"], result["message"], data)

    except Exception as ex:
        return _response("error", str(ex))                  
    
def get_gls_income_expense_list(record: IncomeExpenseRequest):
    try:
        with get_db_connection() as conn: # calling get_db_connection for getting the connection string
            rows = call_db_function(conn, "public.fn_get_gls_income_expense_list", [record.json()]) # calling fn_get_assets_list function from DB  to get data.

            if not rows:
                return _response("failed", "Error Occured While Processing Request")

            result = rows[0]  
            data = result["data"]
            if isinstance(data, str):
                data = json.loads(data)

            return _response(result["status"], result["message"], data)

    except Exception as ex:
        return _response("error", str(ex))        
    

def add_gls_income_expense(record: IncomeExpenseRequest):
    try:
        with get_db_connection() as conn: # calling get_db_connection for getting the connection string
            rows = call_db_function(conn, "public.fn_insert_gls_income_expense", [record.json()]) # calling fn_get_assets_list function from DB  to get data.

            if not rows:
                return _response("failed", "Error Occured While Processing Request")

            result = rows[0]  
            data = result["data"]
            if isinstance(data, str):
                data = json.loads(data)

            return _response(result["status"], result["message"], data)

    except Exception as ex:
        return _response("error", str(ex))  
