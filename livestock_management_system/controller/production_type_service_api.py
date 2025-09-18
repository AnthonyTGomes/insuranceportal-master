from django.http import JsonResponse
from pydantic import ValidationError
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from apiservice.utils import handle_serializer_error, success_response
from rest_framework.response import Response
from rest_framework import status

from common.common_class.util import build_request_with_user
from livestock_management_system.helper.livestock_management_helper_class import get_asset_production_type
from livestock_management_system.helper.model_class import AssetProductionTypeRequest

class ProductionTypeServiceAPIView(APIView):
    permission_classes = [IsAuthenticated]

    """
    @ Author: Tanmay Anthony Gomes
    @ Create Time: 18-Sep-2025 10:27 AM
    @ Modified by: 
    @ Modified time: 
    @ Description: API to get asset production types
    """

    def get(self, request):
        try:
            record = build_request_with_user(AssetProductionTypeRequest, request, method='GET')
            #record = VaccineRequest(**request.data)  # validation happens here        
            result = get_asset_production_type(record)  # validation happens here
            return JsonResponse(result)
        except ValidationError as e:
            return JsonResponse({"status": "failed", "errors": e.errors()}, status=400)         
