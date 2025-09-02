from django.urls import path

from farm_management_system.controller.farm_org_service_api import FarmOrgServiceAPIView


urlpatterns = [
    path('farm-org-service/', FarmOrgServiceAPIView.as_view(), name='farm-org-service'),
]