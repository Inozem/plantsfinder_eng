from django.contrib import admin

from .models import (AutumnLeafColor, BarkColor, FloweringColor,
                     FloweringPeriod, FoliageTypeDeciduous,
                     FruitColor, Hazardous, LeafColor, LeafColorChange,
                     OtherPlantFeature, PlantType, YoungLeafColor)

admin.site.register(PlantType)
admin.site.register(FoliageTypeDeciduous)
admin.site.register(LeafColor)
admin.site.register(LeafColorChange)
admin.site.register(YoungLeafColor)
admin.site.register(AutumnLeafColor)
admin.site.register(FloweringColor)
admin.site.register(FloweringPeriod)
admin.site.register(BarkColor)
admin.site.register(FruitColor)
admin.site.register(OtherPlantFeature)
admin.site.register(Hazardous)
