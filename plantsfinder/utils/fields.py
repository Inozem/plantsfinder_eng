import uuid

from django.db import models


class MultipleChoiceCharField(models.Model):
    """Choice class."""
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
    """Color class."""
    COLOURS = (
        'Black',
        'Blue',
        'Bronzish',
        'Brown',
        'Green',
        'Grey',
        'Orange',
        'Pink',
        'Red',
        'Silver',
        'Violet',
        'White',
        'Yellow',
    )
    CHOICES = tuple((i, i) for i in COLOURS)
    MultipleChoiceCharField._meta.get_field('name').choices = CHOICES

    class Meta:
        abstract = True


class MultipleChoiceMonthsCharField(MultipleChoiceCharField):
    """Months class."""
    MONTHS = (
        'January',
        'February',
        'March',
        'April',
        'May',
        'June',
        'July',
        'August',
        'September',
        'October',
        'November',
        'December',
    )
    CHOICES = tuple((i, i) for i in MONTHS)
    MultipleChoiceCharField._meta.get_field('name').choices = CHOICES

    class Meta:
        ordering = ('name',)
        abstract = True
