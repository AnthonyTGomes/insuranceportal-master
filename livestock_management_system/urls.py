# user_management_system/urls.py
from django.urls import path
from livestock_management_system.controller import livestock_management_api

urlpatterns = [
    path('get-assets/', livestock_management_api.fetch_assets, name='fetch_assets'),
    path('add-health-record/', livestock_management_api.create_health_record, name='create_health_record'),
    path('get-health-record/', livestock_management_api.get_health_record, name='get_health_record'),
    path('get-vaccine-list/', livestock_management_api.get_vaccine_list, name='get_vaccine_list'),
    path('add-asset-vaccination-schedule/', livestock_management_api.create_asset_vaccination_schedule, name='create_asset_vaccination_schedule'),    
    path('get-vaccination-schedule/', livestock_management_api.get_vaccination_schedule, name='get_vaccination_schedule'),  
    path('get-medical-condition/', livestock_management_api.get_medical_condition, name='get_medical_condition'),     
    path('get-medical-condition-severity/', livestock_management_api.get_medical_condition_severity, name='get_medical_condition_severity'),     
    path('get-medical-condition-severity/', livestock_management_api.get_income_expense_list, name='get_income_expense_list'),  
    path('add-income-expense/', livestock_management_api.create_income_expense, name='create_income_expense'),           
]
