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

CHOICES_YES_NO = (('Есть', 'Есть'), ('Нет', 'Нет'))


class NameSynonym(models.Model):
    """Класс названий-синонимов растений."""
    name = models.CharField(
        max_length=250,
        verbose_name='Название растения',
        unique=True,
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Синоним названия растения'
        verbose_name_plural = 'Синонимы названий растений'

    def __str__(self):
        return self.name


class PlantInfo(models.Model):
    """Родительский класс для всех растений."""
    name_species_russian = models.CharField(
        max_length=250,
        verbose_name='Название рода, вида и формы на русском языке',
        null=True,
    )
    name_species_latin = models.CharField(
        max_length=250,
        verbose_name='Название рода, вида и формы на латинском языке',
        null=True,
    )
    name_cultivar = models.CharField(
        max_length=250,
        verbose_name='Название сорта',
        null=True,
        blank=True,
    )
    slug = slug = models.SlugField(
        max_length=75,
        verbose_name='Ссылка',
        unique=True,
    )
    name_synonym = models.ForeignKey(
        NameSynonym,
        related_name='name_synonym',
        verbose_name='Cинонимы названия растения',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    description = models.TextField(
        verbose_name='Описание растения',
        null=True,
        blank=True,
    )
    image = models.ImageField(
        upload_to='image/',
        verbose_name='Изображение',
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ('name_species_russian', 'name_cultivar', )
        unique_together = ('name_species_latin', 'name_cultivar', )

    def __str__(self):
        is_name_cultivar = self.name_cultivar is not None
        name_cultivar = ['', f'"{self.name_cultivar}"'][is_name_cultivar]
        return (f'{self.name_species_russian} {name_cultivar} - '
                f'{self.name_species_latin} {name_cultivar}')


class PlantBasicCharacteristics(PlantInfo):
    """Класс основных характеристик, которые встречаются
    у всех растений вне зависимости от категории.
    """
    usda_zone = models.ManyToManyField(
        UsdaZone,
        related_name='usda_zone',
        verbose_name='Зона морозостойкости',
    )
    sun = models.ManyToManyField(
        Sun,
        related_name='sun',
        verbose_name='Отношение к свету',
    )
    max_height = models.DecimalField(
        verbose_name='Максимальная высота (м)',
        max_digits=5,
        decimal_places=2,
        validators=[MinValueValidator(
            0,
            'Высота растения не может быть меньше 0 м'
        ), MaxValueValidator(
            150,
            'На Земле не существует растений выше 150 м'
        )],
        null=True,
    )
    max_width = models.DecimalField(
        verbose_name='Максимальная ширина (м)',
        max_digits=5,
        decimal_places=2,
        validators=[MinValueValidator(
            0,
            'Ширина растения не может быть меньше 0 м'
        ), MaxValueValidator(
            150,
            'На Земле не существует растений шире 150 м'
        )],
        null=True,
    )


class Deciduous(PlantBasicCharacteristics):
    """Класс лиственных деревьев, кустарников и лиан."""
    fields = {}

    soil_type = models.ManyToManyField(
        SoilType,
        related_name='soil_type',
        verbose_name='Тип почвы',
    )
    soil_moisture = models.ManyToManyField(
        SoilMoisture,
        related_name='soil_moisture',
        verbose_name='Влажность почвы',
    )
    soil_fertility = models.ManyToManyField(
        SoilFertility,
        related_name='soil_fertility',
        verbose_name='Плодородие почвы',
    )
    soil_ph = models.ManyToManyField(
        SoilPh,
        related_name='soil_ph',
        verbose_name='Кислотность почвы',
    )
    life_form = models.ManyToManyField(
        LifeForm,
        related_name='life_form',
        verbose_name='Жизненная форма',
    )
    type_plant_deciduous = models.ManyToManyField(
        TypePlantDeciduous,
        related_name='type_plant_deciduous',
        verbose_name='Тип растения',
    )
    leaves_colour = models.ManyToManyField(
        LeavesColour,
        related_name='leaves_colour',
        verbose_name='Цвет листьев',
    )
    leaves_colour_changes = models.ManyToManyField(
        LeavesColourChanges,
        related_name='leaves_colour_changes',
        verbose_name='Изменение окраски листьев',
    )
    young_leaves_colour = models.ManyToManyField(
        YoungLeavesColour,
        related_name='young_leaves_colour',
        verbose_name='Цвет молодых листьев',
    )
    autumn_leaves_colour = models.ManyToManyField(
        AutumnLeavesColour,
        related_name='autumn_leaves_colour',
        verbose_name='Цвет осенней окраски листьев',
    )
    bloom_colour = models.ManyToManyField(
        BloomColour,
        related_name='bloom_colour',
        verbose_name='Цвет цветов',
    )
    blooming_period = models.ManyToManyField(
        BloomingPeriod,
        related_name='blooming_period',
        verbose_name='Период декоративности цветения',
    )
    fragrance = models.CharField(
        max_length=50,
        choices=CHOICES_YES_NO,
        verbose_name='Наличие аромата',
        null=True,
    )
    bark_colour = models.ManyToManyField(
        BarkColour,
        related_name='bark_colour',
        verbose_name='Цвет коры',
    )
    fruit_colour = models.ManyToManyField(
        FruitColour,
        related_name='fruit_colour',
        verbose_name='Цвет плодов',
    )
    other_types_decoration = models.ManyToManyField(
        OtherTypesDecoration,
        related_name='other_types_decoration',
        verbose_name='Прочие виды декоративности',
    )
    spines = models.CharField(
        max_length=50,
        choices=CHOICES_YES_NO,
        verbose_name='Наличие колючек',
        null=True,
    )
    poison_parts = models.ManyToManyField(
        PoisonParts,
        related_name='poison_parts',
        verbose_name='Ядовитые части',
    )

    class Meta:
        verbose_name = 'Лиственное дерево, кустарник или лиана'
        verbose_name_plural = 'Лиственные деревья, кустарники и лианы'

    def save(self, *args, **kwargs):
        super(self.__class__, self).save(*args, **kwargs)
        self.__class__.fields = get_fields_with_values(self.__class__,
                                                       PlantInfo)
