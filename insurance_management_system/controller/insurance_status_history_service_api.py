from django.http import JsonResponse
from pydantic import ValidationError
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from apiservice.utils import handle_serializer_error, success_response
from rest_framework.response import Response
from rest_framework import status

from common.common_class.util import build_request_with_user
from insurance_management_system.helper.insurance_management_helper_class import update_insurance_status
from insurance_management_system.helper.model_class import InsuranceApplicationRequest

class InsuranceStatusHistoryServiceAPIView(APIView):
    permission_classes = [IsAuthenticated]

    """
    @ Author: Tanmay Anthony Gomes
    @ Create Time: 11-Aug-2025
    @ Modified by: 
    @ Modified time: 
    @ Description: API to Update Insurance Status
    """
    def put(self, request):
        try:
            record = build_request_with_user(InsuranceApplicationRequest, request, method='PUT')
            #record = AssetInfoRequest(**request.data)
            result = update_insurance_status(record)
            return JsonResponse(result)
        except ValidationError as e:
            return JsonResponse({"status": "failed", "errors": e.errors()}, status=400)
        