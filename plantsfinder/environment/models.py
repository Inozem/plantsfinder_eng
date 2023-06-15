from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from utils.fields import MultipleChoiceCharField

CHOICES = {
    'sun': ['Full sun', 'Partial shade', 'Full shade'],
    'soil type': ['Light', 'Semi-heavy', 'Heavy'],
    'soil moisture': ['Drought possible', 'Low', 'Average', 'High',
                      'Flooding possible'],
    'soil fertility': ['Fertile', 'Moderately fertile', 'Poor']
}
MAX_PH_LEVEL = 14
MAX_USDA_ZONE = 12


class UsdaZone(models.Model):
    """USDA zones class."""
    USDA_ZONE_CHOICES = (
        (i, str(i)) for i in range(MAX_USDA_ZONE + 1)
    )
    name = models.PositiveSmallIntegerField(
        verbose_name='Name',
        validators=[MinValueValidator(
            0,
            'USDA zone cannot be less than 0'
        ), MaxValueValidator(
            MAX_USDA_ZONE,
            f'USDA zone cannot be more than {MAX_USDA_ZONE}'
        )],
        choices=USDA_ZONE_CHOICES,
        unique=True
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'USDA zone'
        verbose_name_plural = 'USDA zones'

    def __str__(self):
        return str(self.name)


class Sun(MultipleChoiceCharField):
    """Class attitude of light on plants."""
    CHOICES = tuple((i, i) for i in CHOICES['sun'])
    MultipleChoiceCharField._meta.get_field('name').choices = CHOICES

    class Meta:
        verbose_name = 'Attitude of light'
        verbose_name_plural = 'Attitude of light'


class SoilType(MultipleChoiceCharField):
    """Soil type class."""
    CHOICES = tuple((i, i) for i in CHOICES['soil type'])
    MultipleChoiceCharField._meta.get_field('name').choices = CHOICES

    class Meta:
        verbose_name = 'Soil type'
        verbose_name_plural = 'Soil types'


class SoilMoisture(MultipleChoiceCharField):
    """Soil moisture class."""
    CHOICES = tuple((i, i) for i in CHOICES['soil moisture'])
    MultipleChoiceCharField._meta.get_field('name').choices = CHOICES

    class Meta:
        verbose_name = 'Soil moisture'
        verbose_name_plural = 'Soil moisture'


class SoilFertility(MultipleChoiceCharField):
    """Soil fertility class."""
    CHOICES = tuple((i, i) for i in CHOICES['soil fertility'])
    MultipleChoiceCharField._meta.get_field('name').choices = CHOICES

    class Meta:
        verbose_name = 'Soil fertility'
        verbose_name_plural = 'Soil fertility'


class SoilPh(models.Model):
    """Soil pH class."""
    SOIL_PH_CHOICES = (
        (i / 10, str(i / 10)) for i in range(MAX_PH_LEVEL * 10 + 1)
    )
    name = models.FloatField(
        verbose_name='name',
        validators=[MinValueValidator(
            0,
            'PH level cannot be less than 0'
        ), MaxValueValidator(
            MAX_PH_LEVEL,
            f'PH level cannot be more than {MAX_PH_LEVEL}'
        )],
        choices=SOIL_PH_CHOICES,
        unique=True,
        null=True,
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Soil pH'
        verbose_name_plural = 'Soil pH'

    def __str__(self):
        return str(self.name)
