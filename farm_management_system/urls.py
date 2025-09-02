from django.urls import path

from farm_management_system.controller.farm_org_farmers_service_api import FarmOrgFarmersServiceAPIView
from farm_management_system.controller.farm_org_service_api import FarmOrgServiceAPIView


urlpatterns = [
    path('farm-org-service/', FarmOrgServiceAPIView.as_view(), name='farm-org-service'), 
    path('farm-org-farmers-service/', FarmOrgFarmersServiceAPIView.as_view(), name='farm-org-farmers-service'),
]