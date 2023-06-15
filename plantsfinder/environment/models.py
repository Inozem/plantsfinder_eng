from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from utils.fields import MultipleChoiceCharField

CHOICES = {
    'sun': ['Солнце', 'Полутень', 'Тень'],
    'soil type': ['Легкие', 'Среднетяжелые', 'Тяжелые'],
    'soil moisture': ['Возможна засуха', 'Низкая', 'Умеренная', 'Высокая',
                      'Возможны затопления'],
    'soil fertility': ['Плодородные', 'Умеренно плодородные', 'Бедные']
}
MAX_PH_LEVEL = 14
MAX_USDA_ZONE = 12


class UsdaZone(models.Model):
    """Класс зон морозостойкости."""
    USDA_ZONE_CHOICES = (
        (i, str(i)) for i in range(MAX_USDA_ZONE + 1)
    )
    name = models.PositiveSmallIntegerField(
        verbose_name='Название',
        validators=[MinValueValidator(
            0,
            'Зона морозостойкости не может быть меньше 0'
        ), MaxValueValidator(
            MAX_USDA_ZONE,
            f'Зона морозостойкости не может быть больше {MAX_USDA_ZONE}'
        )],
        choices=USDA_ZONE_CHOICES,
        unique=True
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Зона морозостойкости'
        verbose_name_plural = 'Зоны морозостойкости'

    def __str__(self):
        return str(self.name)


class Sun(MultipleChoiceCharField):
    """Класс отношения растения к свету."""
    CHOICES = tuple((i, i) for i in CHOICES['sun'])
    MultipleChoiceCharField._meta.get_field('name').choices = CHOICES

    class Meta:
        verbose_name = 'Отношение к свету'
        verbose_name_plural = 'Отношение к свету'


class SoilType(MultipleChoiceCharField):
    """Класс типов почвы."""
    CHOICES = tuple((i, i) for i in CHOICES['soil type'])
    MultipleChoiceCharField._meta.get_field('name').choices = CHOICES

    class Meta:
        verbose_name = 'Тип почвы'
        verbose_name_plural = 'Типы почвы'


class SoilMoisture(MultipleChoiceCharField):
    """Класс влажности почвы."""
    CHOICES = tuple((i, i) for i in CHOICES['soil moisture'])
    MultipleChoiceCharField._meta.get_field('name').choices = CHOICES

    class Meta:
        verbose_name = 'Влажность почвы'
        verbose_name_plural = 'Влажность почвы'


class SoilFertility(MultipleChoiceCharField):
    """Класс плодородия почвы."""
    CHOICES = tuple((i, i) for i in CHOICES['soil fertility'])
    MultipleChoiceCharField._meta.get_field('name').choices = CHOICES

    class Meta:
        verbose_name = 'Плодородие почвы'
        verbose_name_plural = 'Плодородие почвы'


class SoilPh(models.Model):
    """Класс кислотности почвы."""
    SOIL_PH_CHOICES = (
        (i / 10, str(i / 10)) for i in range(MAX_PH_LEVEL * 10 + 1)
    )
    name = models.FloatField(
        verbose_name='Название',
        validators=[MinValueValidator(
            0,
            'Уровень кислотности не может быть меньше 0'
        ), MaxValueValidator(
            MAX_PH_LEVEL,
            f'Уровень кислотности не может быть больше {MAX_PH_LEVEL}'
        )],
        choices=SOIL_PH_CHOICES,
        unique=True,
        null=True,
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Кислотность почвы'
        verbose_name_plural = 'Кислотность почвы'

    def __str__(self):
        return str(self.name)
