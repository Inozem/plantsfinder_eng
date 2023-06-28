from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from environment.models import (SoilFertility, SoilMoisture, SoilPh, SoilType,
                                Sun, UsdaZone)
from phytomorphology.models import (AutumnLeavesColour, BarkColour,
                                    BloomColour, BloomingPeriod, FruitColour,
                                    LeavesColour, LeavesColourChanges,
                                    LifeForm, OtherTypesDecoration,
                                    PoisonParts, TypePlantDeciduous,
                                    YoungLeavesColour)
from plants.filters.web_page_filter_fields import get_fields_with_values

CHOICES_YES_NO = (('Has', 'Has'), ('Does not have', 'Does not have'))


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
        verbose_name='Name of the genus, species and form in English',
        null=True,
    )
    name_species_latin = models.CharField(
        max_length=250,
        verbose_name='Name of the genus, species and form in Latin',
        null=True,
    )
    name_cultivar = models.CharField(
        max_length=250,
        verbose_name='Species',
        null=True,
        blank=True,
    )
    slug = slug = models.SlugField(
        max_length=75,
        verbose_name='Link',
        unique=True,
    )
    name_synonym = models.ForeignKey(
        NameSynonym,
        related_name='name_synonym',
        verbose_name='Plant synonym',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    description = models.TextField(
        verbose_name='Plant description',
        null=True,
        blank=True,
    )
    image = models.ImageField(
        upload_to='image/',
        verbose_name='Image',
        null=True,
        blank=True,
    )

    class Meta:
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
        verbose_name='USDA zone',
    )
    sun = models.ManyToManyField(
        Sun,
        related_name='sun',
        verbose_name='Sun exposure',
    )
    max_height = models.DecimalField(
        verbose_name='Maximum height (m)',
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
        verbose_name='Maximum width (m)',
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


class Deciduous(PlantBasicCharacteristics):
    """Class of deciduous trees, shrubs and lianes."""
    fields = {}

    soil_type = models.ManyToManyField(
        SoilType,
        related_name='soil_type',
        verbose_name='Soil type',
    )
    soil_moisture = models.ManyToManyField(
        SoilMoisture,
        related_name='soil_moisture',
        verbose_name='Soil moisture',
    )
    soil_fertility = models.ManyToManyField(
        SoilFertility,
        related_name='soil_fertility',
        verbose_name='Soil fertility',
    )
    soil_ph = models.ManyToManyField(
        SoilPh,
        related_name='soil_ph',
        verbose_name='Soil Ph',
    )
    life_form = models.ManyToManyField(
        LifeForm,
        related_name='life_form',
        verbose_name='Life form',
    )
    type_plant_deciduous = models.ManyToManyField(
        TypePlantDeciduous,
        related_name='type_plant_deciduous',
        verbose_name='Plant type',
    )
    leaves_colour = models.ManyToManyField(
        LeavesColour,
        related_name='leaves_colour',
        verbose_name='Leaves color',
    )
    leaves_colour_changes = models.ManyToManyField(
        LeavesColourChanges,
        related_name='leaf_colour_change',
        verbose_name='Leaf color change',
    )
    young_leaves_colour = models.ManyToManyField(
        YoungLeavesColour,
        related_name='young_leaves_colour',
        verbose_name='Young leaves color',
    )
    autumn_leaves_colour = models.ManyToManyField(
        AutumnLeavesColour,
        related_name='autumn_leaves_colour',
        verbose_name='Autumn leaves color',
    )
    bloom_colour = models.ManyToManyField(
        BloomColour,
        related_name='bloom_colour',
        verbose_name='Flowering color',
    )
    blooming_period = models.ManyToManyField(
        BloomingPeriod,
        related_name='blooming_period',
        verbose_name='Bloom period',
    )
    fragrance = models.CharField(
        max_length=50,
        choices=CHOICES_YES_NO,
        verbose_name='Fragrance',
        null=True,
    )
    bark_colour = models.ManyToManyField(
        BarkColour,
        related_name='bark_colour',
        verbose_name='Bark color',
    )
    fruit_colour = models.ManyToManyField(
        FruitColour,
        related_name='fruit_colour',
        verbose_name='Fruit color',
    )
    other_types_decoration = models.ManyToManyField(
        OtherTypesDecoration,
        related_name='other_types_decoration',
        verbose_name='Other types of decoration',
    )
    spines = models.CharField(
        max_length=50,
        choices=CHOICES_YES_NO,
        verbose_name='Spikes',
        null=True,
    )
    poison_parts = models.ManyToManyField(
        PoisonParts,
        related_name='poison_parts',
        verbose_name='Toison parts',
    )

    class Meta:
        verbose_name = 'Deciduous tree, shrub and liane'
        verbose_name_plural = 'Deciduous trees, shrubs and lianes'

    def save(self, *args, **kwargs):
        super(self.__class__, self).save(*args, **kwargs)
        self.__class__.fields = get_fields_with_values(self.__class__,
                                                       PlantInfo)
