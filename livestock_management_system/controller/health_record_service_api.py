from django.http import JsonResponse
from pydantic import ValidationError
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from apiservice.utils import handle_serializer_error, success_response
from livestock_management_system.helper.livestock_management_helper_class import *
from livestock_management_system.helper.model_class import AssetInfoRequest
from rest_framework import status

class HealthRecordServiceAPIView(APIView):

    permission_classes = [IsAuthenticated] # For Validating Token

    '''
    # @ Author: Tanmay Anthony Gomes
    # @ Create Time: 2025-06-12 12:44:24
    # @ Modified by: Tanmay Anthony Gomes
    # @ Modified time: 
    # @ Description: Api For Inserting Livestock's Health records 
    '''
    def post(self, request):
        try:
            record = HealthRecordRequest(**request.data)  # validation happens here        
            result = add_assets_health_record(record)  # validation happens here
            return JsonResponse(result)
        except ValidationError as e:
            return JsonResponse({"status": "failed", "errors": e.errors()}, status=400)

    '''
    # @ Author: Tanmay Anthony Gomes
    # @ Create Time: 2025-06-11 15:01:24
    # @ Modified by: Tanmay Anthony Gomes
    # @ Modified time: 2025-06-12 17:44:57
    # @ Description: To get Live stock's health records
    '''
    def get(self, request):
        try:
            record = HealthRecordRequest(**request.data)  # validation happens here        
            result = get_assets_health_record(record)  # validation happens here
            return JsonResponse(result)
        except ValidationError as e:
            return JsonResponse({"status": "failed", "errors": e.errors()}, status=400)    