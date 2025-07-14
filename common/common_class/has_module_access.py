

import json
from rest_framework.permissions import BasePermission
from django.db import connection

from common.common_class.common_model_class import AuthUserModuleAccessRequest
from common.common_class.util import _response
from db import call_db_function, get_db_connection

class HasModuleAccess(BasePermission):

    '''
    # @ Author: Tanmay Anthony Gomes
    # @ Create Time: 14-Jul-2025 04:04:15 PM
    # @ Modified by: -
    # @ Modified time: 14-Jul-2025 04:16:37 PM
    # @ Description: Function for getting module access
    '''
    def has_permission(self, request, view):
        user = request.user
        required_module = getattr(view, 'required_module', None)
        
        if not required_module:
            return True  # No module restriction
        
        # Build record to call DB function
        record = AuthUserModuleAccessRequest(
            by_user_id=user.id,
            module_code=required_module
        )
        result = get_auth_module_access(record)
        
        # If it's a dict response from _response() → check status and data
        if result.get("status") != "success":
            return False

        if result.get("data") is None or result.get("data") == []:
            return False

        return True

def get_auth_module_access(record: AuthUserModuleAccessRequest):
    try:
        with get_db_connection() as conn: # calling get_db_connection for getting the connection string
            rows = call_db_function(conn, "public.fn_get_auth_user_module_permission", [record.json()]) # calling fn_get_assets_list function from DB  to get data.

            if not rows:
                return _response("failed", "Error Occured While Processing Request")

            result = rows[0]  
            data = result["data"]
            if isinstance(data, str):
                data = json.loads(data)

            return _response(result["status"], result["message"], data)

    except Exception as ex:
        return _response("error", str(ex))   
    
