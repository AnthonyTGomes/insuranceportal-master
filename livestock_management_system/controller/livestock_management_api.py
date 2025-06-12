import json
from django.http import JsonResponse
from livestock_management_system.helper.livestock_management_helper_class import HealthRecordRequest, get_assets_list, add_assets_health_record
from django.views.decorators.http import require_GET
from pydantic import ValidationError

'''
 # @ Author: Tanmay Anthony Gomes
 # @ Create Time: 2025-06-11 15:00:13
 # @ Modified by: -
 # @ Modified time: -
 # @ Description: APi For Getting Asset List
'''
@require_GET
def fetch_assets(request):
    # Extract pagination params (with defaults)
    start_record = int(request.GET.get("page", 1))
    page_size = int(request.GET.get("size", 10))

    result = get_assets_list(start_record, page_size)
    return JsonResponse(result)

def create_health_record(request):
    # try:
        data = json.loads(request.body)
        record = HealthRecordRequest(**data)  # validation happens here        
        result = add_assets_health_record(record)  # validation happens here
        return JsonResponse(result)
    # except ValidationError as e:
    #     return JsonResponse({"status": "failed", "errors": e.errors()}, status=400)