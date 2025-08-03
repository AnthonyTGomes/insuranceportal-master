from django.urls import path

from insurance_management_system.controller.insurance_application_service_api import InsuranceApplicationServiceAPIView
from insurance_management_system.controller.insurance_product_service_api import InsuranceProductServiceAPIView
from insurance_management_system.controller.farmer_service_api import FarmerServiceAPIView
urlpatterns = [
    path('insurance-application-service/', InsuranceApplicationServiceAPIView.as_view(), name='insurance-application-service'),
    path('insurance-product-service/', InsuranceProductServiceAPIView.as_view(), name='insurance-product-service'), 
    path('farmer-service/', FarmerServiceAPIView.as_view(), name='farmer-service')   
]
