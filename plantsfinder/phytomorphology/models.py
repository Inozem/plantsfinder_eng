from utils.fields import (MultipleChoiceCharField, MultipleChoiceColourField,
                          MultipleChoiceMonthsCharField)

CHOICES = {
    'life form': ['Tree', 'Shrub', 'Ground cover shrub', 'Liana'],
    'type plant': ['Deciduous', 'Semi-evergreen', 'Evergreen'],
    'leaves colour changes': ['Autumn leaf color', 'Color of young leaves',
                              'Not changing'],
    'other types of decoration': ['Decoration in winter',
                                  'Flowers appear before the leaves',
                                  'Flowers appear after the leaves fall',
                                  'Shape of branches', 'No other types'],
    'poison parts': ['Bark', 'Roots', 'Leaves', 'Fruits', 'Seeds', 'Sap',
                     'Flowers', 'Not poisonous'],
}


class LifeForm(MultipleChoiceCharField):
    """Life form class."""
    CHOICES = tuple((i, i) for i in CHOICES['life form'])
    MultipleChoiceCharField._meta.get_field('name').choices = CHOICES

    class Meta:
        verbose_name = 'Plant life form'
        verbose_name_plural = 'Plant life forms'


class TypePlantDeciduous(MultipleChoiceCharField):
    """Deciduous plant type class."""
    CHOICES = tuple((i, i) for i in CHOICES['type plant'])
    MultipleChoiceCharField._meta.get_field('name').choices = CHOICES

    class Meta:
        verbose_name = 'Plant type'
        verbose_name_plural = 'plant types'


class LeavesColour(MultipleChoiceColourField):
    """Leaves color class."""
    class Meta:
        verbose_name = 'Leaves color'
        verbose_name_plural = 'Leaves colors'


class LeavesColourChanges(MultipleChoiceCharField):
    """Class of seasonal leaves color change."""
    CHOICES = tuple((i, i) for i in CHOICES['leaves colour changes'])
    MultipleChoiceCharField._meta.get_field('name').choices = CHOICES

    class Meta:
        verbose_name = 'Seasonal leaves color change'
        verbose_name_plural = 'Seasonal leaves color changes'


class YoungLeavesColour(MultipleChoiceColourField):
    """Young leaves color class."""
    class Meta:
        verbose_name = 'Young leaves color'
        verbose_name_plural = 'Young leaves colors'


class AutumnLeavesColour(MultipleChoiceColourField):
    """Autumn leaf color class."""
    class Meta:
        verbose_name = 'Autumn leaf color'
        verbose_name_plural = 'Autumn leaf colors'


class BloomColour(MultipleChoiceColourField):
    """Flower color class."""
    ADDITIONAL_CHOICES = ('Is not decorative', 'Does not have')
    CHOICES = tuple((i, i) for i in ADDITIONAL_CHOICES)
    MultipleChoiceColourField._meta.get_field('name').choices += CHOICES

    class Meta:
        verbose_name = 'Flower color'
        verbose_name_plural = 'Flower colors'


class BloomingPeriod(MultipleChoiceMonthsCharField):
    """Bloom season class."""
    CHOICES = (('Does not have', 'Does not have'), )
    MultipleChoiceMonthsCharField._meta.get_field('name').choices += CHOICES

    class Meta:
        verbose_name = 'Bloom season'
        verbose_name_plural = 'Bloom seasons'


class BarkColour(MultipleChoiceColourField):
    """Bark color class."""
    class Meta:
        verbose_name = 'Bark color'
        verbose_name_plural = 'Bark colorы'


class FruitColour(MultipleChoiceColourField):
    """Fruit color class."""
    class Meta:
        verbose_name = 'Fruit color'
        verbose_name_plural = 'Fruit color'


class OtherTypesDecoration(MultipleChoiceCharField):
    """Class of other types of decoration."""
    CHOICES = tuple((i, i) for i in CHOICES['other types of decoration'])
    MultipleChoiceCharField._meta.get_field('name').choices = CHOICES

    class Meta:
        verbose_name = 'Other type of decoration'
        verbose_name_plural = 'Other types of decoration'


class PoisonParts(MultipleChoiceCharField):
    """Class of poisonous plant parts."""
    CHOICES = tuple((i, i) for i in CHOICES['poison parts'])
    MultipleChoiceCharField._meta.get_field('name').choices = CHOICES

    class Meta:
        verbose_name = 'Poisonous plant part'
        verbose_name_plural = 'Poisonous plant parts'
