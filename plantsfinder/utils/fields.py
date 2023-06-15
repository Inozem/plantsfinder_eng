import uuid

from django.db import models


class MultipleChoiceCharField(models.Model):
    CHOICES = ()
    name = models.CharField(
        max_length=50,
        verbose_name='Name',
        choices=CHOICES,
        unique=True,
        default=uuid.uuid1,
    )

    class Meta:
        ordering = ('id',)
        abstract = True

    def __str__(self):
        return self.name


class MultipleChoiceColourField(MultipleChoiceCharField):
    """Класс цветов."""
    COLOURS = (
        'Белый',
        'Бронзоватый',
        'Голубой',
        'Желтый',
        'Зеленый',
        'Коричневый',
        'Красный',
        'Оранжевый',
        'Розовый',
        'Серебристый',
        'Серый',
        'Сизый',
        'Синий',
        'Фиолетовый',
        'Черный',
    )
    CHOICES = tuple((i, i) for i in COLOURS)
    MultipleChoiceCharField._meta.get_field('name').choices = CHOICES

    class Meta:
        abstract = True


class MultipleChoiceMonthsCharField(MultipleChoiceCharField):
    """Класс цветов."""
    MONTHS = (
        'Январь',
        'Февраль',
        'Март',
        'Апрель',
        'Май',
        'Июнь',
        'Июль',
        'Август',
        'Сентябрь',
        'Октябрь',
        'Ноябрь',
        'Декабрь',
    )
    CHOICES = tuple((i, i) for i in MONTHS)
    MultipleChoiceCharField._meta.get_field('name').choices = CHOICES

    class Meta:
        ordering = ('name',)
        abstract = True
