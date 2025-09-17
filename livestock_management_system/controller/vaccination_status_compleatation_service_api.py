from django.http import JsonResponse
from pydantic import ValidationError
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from apiservice.utils import handle_serializer_error, success_response
from rest_framework.response import Response
from rest_framework import status

from common.common_class.util import build_request_with_user
from livestock_management_system.helper.livestock_management_helper_class import update_asset_vaccination_schedule_status
from livestock_management_system.helper.model_class import VaccinationScheduleRequest

class VaccinationStatusCompleatationServiceAPIView(APIView):
    permission_classes = [IsAuthenticated]

    """
    @ Author: Tanmay Anthony Gomes
    @ Create Time: 17-Sep-2025 05:01 PM
    @ Modified by: 
    @ Modified time: 
    @ Description: API to update Asset's Vaccination schedule's status
    """
    def put(self, request):
        try:
            record = build_request_with_user(VaccinationScheduleRequest, request, method='PUT')
            print (record)
            #record = AssetInfoRequest(**request.data)
            result = update_asset_vaccination_schedule_status(record)
            return JsonResponse(result)
        except ValidationError as e:
            return JsonResponse({"status": "failed", "errors": e.errors()}, status=400)
        
