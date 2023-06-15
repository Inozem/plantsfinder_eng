from django.contrib import admin

from .models import (AutumnLeavesColour, BarkColour, BloomColour,
                     BloomingPeriod, FruitColour, LeavesColour,
                     LeavesColourChanges, LifeForm, OtherTypesDecoration,
                     PoisonParts, TypePlantDeciduous, YoungLeavesColour)

admin.site.register(LifeForm)
admin.site.register(TypePlantDeciduous)
admin.site.register(LeavesColour)
admin.site.register(LeavesColourChanges)
admin.site.register(YoungLeavesColour)
admin.site.register(AutumnLeavesColour)
admin.site.register(BloomColour)
admin.site.register(BloomingPeriod)
admin.site.register(BarkColour)
admin.site.register(FruitColour)
admin.site.register(OtherTypesDecoration)
admin.site.register(PoisonParts)
