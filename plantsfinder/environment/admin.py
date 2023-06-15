from django.contrib import admin

from .models import (SoilFertility, SoilMoisture, SoilPh, SoilType, Sun,
                     UsdaZone)

admin.site.register(UsdaZone)
admin.site.register(Sun)
admin.site.register(SoilType)
admin.site.register(SoilMoisture)
admin.site.register(SoilFertility)
admin.site.register(SoilPh)
