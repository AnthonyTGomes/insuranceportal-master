from django.http import JsonResponse
from pydantic import ValidationError
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from apiservice.utils import handle_serializer_error, success_response
from livestock_management_system.helper.livestock_management_helper_class import *
from livestock_management_system.helper.model_class import AssetInfoRequest
from rest_framework import status

class MedicalConditionSeverityServiceAPIView(APIView):

    permission_classes = [IsAuthenticated] # For Validating Token

    '''
    # @ Author: Tanmay Anthony Gomes
    # @ Create Time: 2025-06-11 15:00:13
    # @ Modified by: Tanmay Anthony Gomes
    # @ Modified time: 2025-06-15 11:04:31
    # @ Description: This api will get the medical condition severity types
    '''
    def get(self, request):
        try:
            data = json.loads(request.body)
            record = AssetMedicalConditionSeverityRequest(**data)  # validation happens here        
            result = get_asset_medical_condition_severity(record)  # validation happens here
            return JsonResponse(result)
        except ValidationError as e:
            return JsonResponse({"status": "failed", "errors": e.errors()}, status=400)  