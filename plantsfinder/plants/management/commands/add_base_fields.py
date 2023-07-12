from django.core.management.base import BaseCommand

from environment.models import (SoilFertility, SoilMoisture, SoilPh, SoilType,
                                Sun, UsdaZone)
from phytomorphology.models import (AutumnLeafColor, BarkColor, FloweringColor,
                                    FloweringPeriod, FoliageTypeDeciduous,
                                    FruitColor, Hazardous, LeafColor,
                                    LeafColorChange, OtherPlantFeature,
                                    PlantType, YoungLeafColor)

MODELS_M2M_CHOICES = (UsdaZone, Sun, SoilType, SoilMoisture, SoilFertility,
                      SoilPh, AutumnLeafColor, BarkColor, FloweringColor,
                      FloweringPeriod, FruitColor, LeafColor,
                      LeafColorChange, PlantType, OtherPlantFeature,
                      Hazardous, FoliageTypeDeciduous, YoungLeafColor)


class Command(BaseCommand):
    """Creates values for ManyToMany fields."""
    help = 'Creates values for ManyToMany fields.'

    def handle(self, *args, **options):
        for model in MODELS_M2M_CHOICES:
            for choice in model._meta.get_field('name').choices:
                model.objects.create(name=choice[0])
