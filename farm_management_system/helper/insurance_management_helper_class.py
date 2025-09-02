import psycopg2
from django.conf import settings
import json
from common.common_class.util import _response
from db import *
from farm_management_system.helper.model_class import FarmOrgFarmersInfoRequest, FarmOrgInfoRequest

'''
 # @ Author: Tanmay Anthony Gomes
 # @ Create Time: 
 # @ Modified by: Tanmay Anthony Gomes
 # @ Modified time: 
 # @ Description: Function for inserting farm organizartions into DB
'''
def insert_farm_organizations(record: FarmOrgInfoRequest):
    try:
        with get_db_connection() as conn: # calling get_db_connection for getting the connection string
            rows = call_db_function(conn, "public.fn_insert_farm_organizations", [record.json()]) # calling fn_get_assets_list function from DB  to get data.

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
 # @ Create Time: 
 # @ Modified by: Tanmay Anthony Gomes
 # @ Modified time: 
 # @ Description: Function for inserting farm organizartions into DB
'''
def update_farm_organizations(record: FarmOrgInfoRequest):
    try:
        with get_db_connection() as conn: # calling get_db_connection for getting the connection string
            rows = call_db_function(conn, "public.fn_update_farm_organizations", [record.json()]) # calling fn_get_assets_list function from DB  to get data.

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
 # @ Create Time: 
 # @ Modified by: Tanmay Anthony Gomes
 # @ Modified time: 
 # @ Description: Function for getting farm organizartions List
'''
def get_farm_organization_list(record: FarmOrgInfoRequest):
    try:
        with get_db_connection() as conn: # calling get_db_connection for getting the connection string
            rows = call_db_function(conn, "public.fn_get_farm_organization_list", [record.json()]) # calling fn_get_assets_list function from DB  to get data.

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
 # @ Create Time: 
 # @ Modified by: Tanmay Anthony Gomes
 # @ Modified time: 
 # @ Description: Function for inserting farm organizartions farmers into DB
'''
def insert_farm_org_farmers(record: FarmOrgFarmersInfoRequest):
    try:
        with get_db_connection() as conn: # calling get_db_connection for getting the connection string
            rows = call_db_function(conn, "public.fn_insert_farm_org_farmers", [record.json()]) # calling fn_get_assets_list function from DB  to get data.

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
 # @ Create Time: 
 # @ Modified by: Tanmay Anthony Gomes
 # @ Modified time: 
 # @ Description: Function for updating farm organizartions farmers into DB
'''
def update_farm_org_farmers(record: FarmOrgFarmersInfoRequest):
    try:
        with get_db_connection() as conn: # calling get_db_connection for getting the connection string
            rows = call_db_function(conn, "public.fn_update_farm_org_farmers", [record.json()]) # calling fn_get_assets_list function from DB  to get data.

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
 # @ Create Time: 
 # @ Modified by: Tanmay Anthony Gomes
 # @ Modified time: 
 # @ Description: Function for getting farm organizartions farmers list into DB
'''
def get_farm_org_farmer_list(record: FarmOrgFarmersInfoRequest):
    try:
        with get_db_connection() as conn: # calling get_db_connection for getting the connection string
            rows = call_db_function(conn, "public.fn_get_farm_org_farmer_list", [record.json()]) # calling fn_get_assets_list function from DB  to get data.

            if not rows:
                return _response("failed", "Error Occured While Processing Request")

            result = rows[0]  
            data = result["data"]
            if isinstance(data, str):
                data = json.loads(data)

            return _response(result["status"], result["message"], data)

    except Exception as ex:
        return _response("error", str(ex))      