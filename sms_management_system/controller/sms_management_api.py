import json
from django.http import JsonResponse
from pydantic import ValidationError
from sms_management_system.helper.model_class import SendSMSRequest
from sms_management_system.helper.sms_management_helper_class import send_sms_request

'''
 # @ Author: Tanmay Anthony Gomes
 # @ Create Time: 2025-06-11 15:00:13
 # @ Modified by: Tanmay Anthony Gomes
 # @ Modified time: 2025-06-18 11:04:31
 # @ Description: This api will Send The Request to the providers server to send SMS
 '''
def send_sms(request):
     try:
        data = json.loads(request.body)
        record = SendSMSRequest(**data)  # validation happens here        
        result = send_sms_request(record)  # validation happens here
        return JsonResponse(result)
     except ValidationError as e:
         return JsonResponse({"status": "failed", "errors": e.errors()}, status=400)    