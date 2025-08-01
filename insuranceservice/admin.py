from django.contrib import admin

from insuranceservice.models import *

# Register your models here.
admin.site.register(InsuranceCompany)
admin.site.register(InsuranceType)
admin.site.register(InsurancePeriod)
admin.site.register(PremiumPercentage)
admin.site.register(InsuranceCategory)
admin.site.register(InsuranceProduct)
admin.site.register(AssetInsurance)
admin.site.register(InsuranceClaim)
admin.site.register(ClaimDocument)
