from utils.fields import (MultipleChoiceCharField, MultipleChoiceColorField,
                          MultipleChoiceMonthsCharField)

CHOICES = {
    'plant type': ['Tree', 'Shrub', 'Ground cover shrub', 'Liana'],
    'foliage type': ['Deciduous', 'Semi-evergreen', 'Evergreen'],
    'leaf color change': ['Autumn foliage color', 'Young leaf color',
                          'No change'],
    'other plant features': ['Decorative in winter', 'Flowers before leaves',
                             'Flowers after leaves fall', 'No other features'],
    'hazardous': ['Toxic', 'Thorny', 'Not hazardous'],
}


class PlantType(MultipleChoiceCharField):
    """Plant type class."""
    CHOICES = tuple((i, i) for i in CHOICES['plant type'])
    MultipleChoiceCharField._meta.get_field('name').choices = CHOICES

    class Meta:
        verbose_name = 'Plant type'
        verbose_name_plural = 'Plant types'


class FoliageTypeDeciduous(MultipleChoiceCharField):
    """Deciduous foliage type class."""
    CHOICES = tuple((i, i) for i in CHOICES['foliage type'])
    MultipleChoiceCharField._meta.get_field('name').choices = CHOICES

    class Meta:
        verbose_name = 'Foliage type'
        verbose_name_plural = 'Foliage types'


class LeafColor(MultipleChoiceColorField):
    """Leaves color class."""
    class Meta:
        verbose_name = 'Leaf color'
        verbose_name_plural = 'Leaf colors'


class LeafColorChange(MultipleChoiceCharField):
    """Class of seasonal leaves color change."""
    CHOICES = tuple((i, i) for i in CHOICES['leaf color change'])
    MultipleChoiceCharField._meta.get_field('name').choices = CHOICES

    class Meta:
        verbose_name = 'Leaf color change'
        verbose_name_plural = 'Leaf color change'


class YoungLeafColor(MultipleChoiceColorField):
    """Young leaves color class."""
    class Meta:
        verbose_name = 'Young leaf color'
        verbose_name_plural = 'Young leaf colors'


class AutumnLeafColor(MultipleChoiceColorField):
    """Autumn leaf color class."""
    class Meta:
        verbose_name = 'Autumn leaf color'
        verbose_name_plural = 'Autumn leaf colors'


class FloweringColor(MultipleChoiceColorField):
    """Flower color class."""
    ADDITIONAL_CHOICES = ('Not vivid', 'Non-flowering')
    CHOICES = tuple((i, i) for i in ADDITIONAL_CHOICES)
    MultipleChoiceColorField._meta.get_field('name').choices += CHOICES

    class Meta:
        verbose_name = 'Flowering color'
        verbose_name_plural = 'Flowering colors'


class FloweringPeriod(MultipleChoiceMonthsCharField):
    """Bloom season class."""
    CHOICES = (('Non-flowering', 'Non-flowering'), )
    MultipleChoiceMonthsCharField._meta.get_field('name').choices += CHOICES

    class Meta:
        verbose_name = 'Flowering period'
        verbose_name_plural = 'Flowering periods'


class BarkColor(MultipleChoiceColorField):
    """Bark color class."""
    class Meta:
        verbose_name = 'Bark color'
        verbose_name_plural = 'Bark colors'


class FruitColor(MultipleChoiceColorField):
    """Fruit color class."""
    CHOICES = (('No fruits', 'No fruits'), )
    MultipleChoiceColorField._meta.get_field('name').choices += CHOICES

    class Meta:
        verbose_name = 'Fruit color'
        verbose_name_plural = 'Fruit color'


class OtherPlantFeature(MultipleChoiceCharField):
    """Class of other types of decoration."""
    CHOICES = tuple((i, i) for i in CHOICES['other plant features'])
    MultipleChoiceCharField._meta.get_field('name').choices = CHOICES

    class Meta:
        verbose_name = 'Other plant feature'
        verbose_name_plural = 'Other plant features'


class Hazardous(MultipleChoiceCharField):
    """Plant hazard class."""
    CHOICES = tuple((i, i) for i in CHOICES['hazardous'])
    MultipleChoiceCharField._meta.get_field('name').choices = CHOICES

    class Meta:
        verbose_name = 'Hazardous'
        verbose_name_plural = 'Hazardous'
