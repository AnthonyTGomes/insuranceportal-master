# user_management_system/urls.py
from django.urls import path
from livestock_management_system.controller import livestock_management_api

urlpatterns = [
    path('get-assets/', livestock_management_api.fetch_assets, name='fetch_assets'),
    path('add-health-record/', livestock_management_api.create_health_record, name='create_health_record'),
    path('get-health-record/', livestock_management_api.get_health_record, name='get_health_record'),
]
