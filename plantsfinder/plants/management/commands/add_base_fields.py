from django.core.management.base import BaseCommand

from environment.models import (SoilFertility, SoilMoisture, SoilPh, SoilType,
                                Sun, UsdaZone)
from phytomorphology.models import (AutumnLeavesColour, BarkColour,
                                    BloomColour, BloomingPeriod, FruitColour,
                                    LeavesColour, LeavesColourChanges,
                                    LifeForm, OtherTypesDecoration,
                                    PoisonParts, TypePlantDeciduous,
                                    YoungLeavesColour)

MODELS_M2M_CHOICES = (UsdaZone, Sun, SoilType, SoilMoisture, SoilFertility,
                      SoilPh, AutumnLeavesColour, BarkColour, BloomColour,
                      BloomingPeriod, FruitColour, LeavesColour,
                      LeavesColourChanges, LifeForm, OtherTypesDecoration,
                      PoisonParts, TypePlantDeciduous, YoungLeavesColour)


class Command(BaseCommand):
    """Загрузка значений выбора для полей ManyToMany."""
    help = 'Создает списки значений для выбора.'

    def handle(self, *args, **options):
        for model in MODELS_M2M_CHOICES:
            for choice in model._meta.get_field('name').choices:
                model.objects.create(name=choice[0])
