from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from environment.models import (SoilFertility, SoilMoisture, SoilPh, SoilType,
                                Sun, UsdaZone)
from phytomorphology.models import (AutumnLeafColor, BarkColor, FloweringColor,
                                    FloweringPeriod, FoliageTypeDeciduous,
                                    FruitColor, Hazardous, LeafColor,
                                    LeafColorChange, OtherPlantFeature,
                                    PlantType, YoungLeafColor)
from plants.filters.web_page_filter_fields import get_fields_with_values

CHOICES_YES_NO = (('Yes', 'Yes'), ('No', 'No'))


class NameSynonym(models.Model):
    """Plant synonym class."""
    name = models.CharField(
        max_length=250,
        verbose_name='Name of a plant',
        unique=True,
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Plant synonym'
        verbose_name_plural = 'Plant synonyms'

    def __str__(self):
        return self.name


class PlantInfo(models.Model):
    """Parent class for all plants."""
    name_species_english = models.CharField(
        max_length=250,
        verbose_name='name of the genus, species and form in English',
        null=True,
    )
    name_species_latin = models.CharField(
        max_length=250,
        verbose_name='name of the genus, species and form in Latin',
        null=True,
    )
    name_cultivar = models.CharField(
        max_length=250,
        verbose_name='species',
        null=True,
        blank=True,
    )
    slug = slug = models.SlugField(
        max_length=75,
        verbose_name='link',
        unique=True,
    )
    name_synonym = models.ForeignKey(
        NameSynonym,
        related_name='name_synonym',
        verbose_name='plant synonym',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    description = models.TextField(
        verbose_name='plant description',
        null=True,
        blank=True,
    )
    image = models.ImageField(
        upload_to='image/',
        verbose_name='image',
        null=True,
        blank=True,
    )

    class Meta:
        abstract = True
        ordering = ('name_species_english', 'name_cultivar', )
        unique_together = ('name_species_latin', 'name_cultivar', )

    def __str__(self):
        is_name_cultivar = self.name_cultivar is not None
        name_cultivar = ['', f'"{self.name_cultivar}"'][is_name_cultivar]
        return (f'{self.name_species_english} {name_cultivar} - '
                f'{self.name_species_latin} {name_cultivar}')


class PlantBasicCharacteristics(PlantInfo):
    """
    A class of basic characteristics that are found in all plants,
    regardless of category.
    """
    usda_zone = models.ManyToManyField(
        UsdaZone,
        related_name='usda_zone',
        verbose_name='hardiness zone (usda)',
    )
    sun = models.ManyToManyField(
        Sun,
        related_name='sun',
        verbose_name='sunlight',
    )
    max_height = models.DecimalField(
        verbose_name='maximum height range (meters)',
        max_digits=5,
        decimal_places=2,
        validators=[MinValueValidator(
            0,
            'The height of the plant cannot be less 0 m'
        ), MaxValueValidator(
            150,
            'There are no plants on Earth higher than 150 m'
        )],
        null=True,
    )
    max_width = models.DecimalField(
        verbose_name='maximum width range (meters)',
        max_digits=5,
        decimal_places=2,
        validators=[MinValueValidator(
            0,
            'The width of the plant cannot be less 0 m'
        ), MaxValueValidator(
            150,
            'There are no plants on Earth wider than 150 m'
        )],
        null=True,
    )

    class Meta:
        abstract = True


class SoilGroup(models.Model):
    soil_type = models.ManyToManyField(
        SoilType,
        related_name='soil_type',
        verbose_name='soil type',
    )
    soil_moisture = models.ManyToManyField(
        SoilMoisture,
        related_name='soil_moisture',
        verbose_name='soil moisture level',
    )
    soil_fertility = models.ManyToManyField(
        SoilFertility,
        related_name='soil_fertility',
        verbose_name='soil fertility',
    )
    soil_ph = models.ManyToManyField(
        SoilPh,
        related_name='soil_ph',
        verbose_name='soil ph',
    )

    class Meta:
        abstract = True


class PlantTypeGroup(models.Model):
    plant_type = models.ManyToManyField(
        PlantType,
        related_name='plant_type',
        verbose_name='plant type',
    )
    foliage_type_deciduous = models.ManyToManyField(
        FoliageTypeDeciduous,
        related_name='foliage_type_deciduous',
        verbose_name='foliage type',
    )

    class Meta:
        abstract = True


class LeafColorGroup(models.Model):
    leaf_color = models.ManyToManyField(
        LeafColor,
        related_name='leaf_color',
        verbose_name='leaf color',
    )
    leaf_color_change = models.ManyToManyField(
        LeafColorChange,
        related_name='leaf_colour_change',
        verbose_name='leaf color change',
    )
    young_leaf_color = models.ManyToManyField(
        YoungLeafColor,
        related_name='young_leaf_color',
        verbose_name='young leaf color',
    )
    autumn_leaf_color = models.ManyToManyField(
        AutumnLeafColor,
        related_name='autumn_leaf_color',
        verbose_name='autumn leaf color',
    )

    class Meta:
        abstract = True


class FloweringGroup(models.Model):
    flowering_color = models.ManyToManyField(
        FloweringColor,
        related_name='flowering_color',
        verbose_name='flowering color',
    )
    flowering_period = models.ManyToManyField(
        FloweringPeriod,
        related_name='flowering_period',
        verbose_name='flowering period',
    )
    scent = models.CharField(
        max_length=50,
        choices=CHOICES_YES_NO,
        verbose_name='scent',
        null=True,
    )

    class Meta:
        abstract = True


class BarkColorGroup(models.Model):
    bark_color = models.ManyToManyField(
        BarkColor,
        related_name='bark_color',
        verbose_name='bark color',
    )

    class Meta:
        abstract = True


class FruitColorGroup(models.Model):
    fruit_color = models.ManyToManyField(
        FruitColor,
        related_name='fruit_color',
        verbose_name='fruit color',
    )

    class Meta:
        abstract = True


class OtherPlantsFeaturesGroup(models.Model):
    other_plant_features = models.ManyToManyField(
        OtherPlantFeature,
        related_name='other_plant_features',
        verbose_name='other plant features',
    )

    class Meta:
        abstract = True


class HazardousGroup(models.Model):
    hazardous = models.ManyToManyField(
        Hazardous,
        related_name='hazardous',
        verbose_name='hazardous',
    )

    class Meta:
        abstract = True


class Deciduous(PlantBasicCharacteristics, SoilGroup, PlantTypeGroup, LeafColorGroup, FloweringGroup, BarkColorGroup, FruitColorGroup, OtherPlantsFeaturesGroup, HazardousGroup):
    """Class of deciduous trees, shrubs and lianes."""
    fields = {}

    class Meta:
        verbose_name = 'Deciduous tree, shrub and liane'
        verbose_name_plural = 'Deciduous trees, shrubs and lianes'

    def save(self, *args, **kwargs):
        super(self.__class__, self).save(*args, **kwargs)
        self.__class__.fields = get_fields_with_values(self.__class__,
                                                       PlantInfo)
