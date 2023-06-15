from utils.fields import (MultipleChoiceCharField, MultipleChoiceColourField,
                          MultipleChoiceMonthsCharField)

CHOICES = {
    'life form': ['Дерево', 'Кустарник', 'Почвопокровный кустарник', 'Лиана'],
    'type plant': ['Листопадное', 'Полувечнозеленое', 'Вечнозеленое'],
    'leaves colour changes': ['Осенняя окраска', 'Молодые листья',
                              'Отсутствует'],
    'other types of decoration': ['Декоративность в зимний период',
                                  'Цветки до появления листьев',
                                  'Цветки после опадания листьев',
                                  'Форма ветвей', 'Отсутствуют'],
    'poison parts': ['Кора', 'Корни', 'Листья', 'Плоды', 'Семена', 'Сок',
                     'Цветы', 'Отсутствуют'],
}


class LifeForm(MultipleChoiceCharField):
    """Класс жизненной формы растений."""
    CHOICES = tuple((i, i) for i in CHOICES['life form'])
    MultipleChoiceCharField._meta.get_field('name').choices = CHOICES

    class Meta:
        verbose_name = 'Жизненная форма растения'
        verbose_name_plural = 'Жизненные формы растений'


class TypePlantDeciduous(MultipleChoiceCharField):
    """Класс типов лиственных растений."""
    CHOICES = tuple((i, i) for i in CHOICES['type plant'])
    MultipleChoiceCharField._meta.get_field('name').choices = CHOICES

    class Meta:
        verbose_name = 'Тип растения'
        verbose_name_plural = 'Типы растений'


class LeavesColour(MultipleChoiceColourField):
    """Класс цвета листьев."""
    class Meta:
        verbose_name = 'Цвет листьев'
        verbose_name_plural = 'Цвета листвьев'


class LeavesColourChanges(MultipleChoiceCharField):
    """Класс сезонного изменения окраски листьев."""
    CHOICES = tuple((i, i) for i in CHOICES['leaves colour changes'])
    MultipleChoiceCharField._meta.get_field('name').choices = CHOICES

    class Meta:
        verbose_name = 'Изменение окраски листьев'
        verbose_name_plural = 'Изменения окраски листьев'


class YoungLeavesColour(MultipleChoiceColourField):
    """Класс цвета молодых листьев."""
    class Meta:
        verbose_name = 'Цвет молодых листьев'
        verbose_name_plural = 'Цвета молодых листвьев'


class AutumnLeavesColour(MultipleChoiceColourField):
    """Класс цвета осенней окраски листьев."""
    class Meta:
        verbose_name = 'Осенняя окраска листьев'
        verbose_name_plural = 'Осенняя окраска листьев'


class BloomColour(MultipleChoiceColourField):
    """Класс цвета цветов."""
    ADDITIONAL_CHOICES = ('Не являются декоративными', 'Отсутствуют')
    CHOICES = tuple((i, i) for i in ADDITIONAL_CHOICES)
    MultipleChoiceColourField._meta.get_field('name').choices += CHOICES

    class Meta:
        verbose_name = 'Цвет цветов'
        verbose_name_plural = 'Цвета цветов'


class BloomingPeriod(MultipleChoiceMonthsCharField):
    """Класс периода цветения."""
    CHOICES = (('Отсутствует', 'Отсутствует'), )
    MultipleChoiceMonthsCharField._meta.get_field('name').choices += CHOICES

    class Meta:
        verbose_name = 'Период цветения'
        verbose_name_plural = 'Периоды цветения'


class BarkColour(MultipleChoiceColourField):
    """Класс цвета коры."""
    class Meta:
        verbose_name = 'Цвет коры'
        verbose_name_plural = 'Цвета коры'


class FruitColour(MultipleChoiceColourField):
    """Класс цвета плодов."""
    class Meta:
        verbose_name = 'Цвет плодов'
        verbose_name_plural = 'Цвета плодов'


class OtherTypesDecoration(MultipleChoiceCharField):
    """Класс прочих видов декоративности."""
    CHOICES = tuple((i, i) for i in CHOICES['other types of decoration'])
    MultipleChoiceCharField._meta.get_field('name').choices = CHOICES

    class Meta:
        verbose_name = 'Прочие виды декоратичности'
        verbose_name_plural = 'Прочие виды декоратичности'


class PoisonParts(MultipleChoiceCharField):
    """Класс ядовитых частей."""
    CHOICES = tuple((i, i) for i in CHOICES['poison parts'])
    MultipleChoiceCharField._meta.get_field('name').choices = CHOICES

    class Meta:
        verbose_name = 'Ядовитые части'
        verbose_name_plural = 'Ядовитые части'
