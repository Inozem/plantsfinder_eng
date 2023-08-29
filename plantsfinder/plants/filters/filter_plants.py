import time

from django.db.models import Max, Min, Q
from django.utils.datastructures import MultiValueDictKeyError


def get_clean_words(text):
    """
    Return list of words without unwanted symbols.
    """
    unwanted_symbols = '.,":?!;-/~`' + "'"
    translate_symbols = {ord(sym): None for sym in unwanted_symbols}
    text = text.translate(translate_symbols)
    words = []
    if ' ' in text:
        words = [word for word in text.split(' ') if word != '']
    else:
        words = [text]
    return words


def filter_plants_with_plant_name(plants, text):
    """
    Filters plants according to the plant name in request.
    If plant has this text in his name or in one of synonym names.
    """
    words = get_clean_words(text)
    for word in words:
        plants = plants.exclude(
            ~Q(name_species_english__iregex=word) &
            ~Q(name_species_latin__iregex=word) &
            ~Q(name_cultivar__iregex=word) &
            ~Q(name_synonym__name__iregex=word))
    return plants


def filter_plants_min_max(plants, filters, filter_name):
    """
    Returns plants filtered by filters that contain minimum and maximum values.
    """
    filter_suffixes = {
        '_min': '__lt',
        '_max': '__gt',
    }
    if 'soil_ph' in filter_name:
        if '_max' in filter_name:
            plants = plants.annotate(soil_ph_min=Min('soil_ph__name'))
            filter_suffixes['_max'] = '_min__gt'
        elif '_min' in filter_name:
            plants = plants.annotate(soil_ph_max=Max('soil_ph__name'))
            filter_suffixes['_min'] = '_max__lt'
    suffix = filter_name[-4:]
    new_suffix = filter_suffixes[suffix]
    filter_name_compare = filter_name.replace(suffix, new_suffix)
    filter_value = float(filters[filter_name])
    plants = plants.exclude(**{filter_name_compare: filter_value})
    return plants


def filter_plants(plants, filters):
    """
    Filters plants according to the request and
    creates a variable with the minimum and maximum values of the filters
    (if they were in the request).
    """
    start = time.time()
    filters_min_max = {}
    try:
        plant_name = filters['plant_name']
        if plant_name:
            plants = filter_plants_with_plant_name(plants, plant_name)
    except MultiValueDictKeyError:
        pass
    if plants:
        for filter_name in filters:
            if (('_min' in filter_name or '_max' in filter_name)
                    and (filters[filter_name] != '')):
                plants = filter_plants_min_max(plants, filters, filter_name)
                filters_min_max[filter_name] = filters[filter_name]
            elif (filter_name not in ('page', 'plant_name')
                  and filters[filter_name] != ''):
                filter_values = filters.getlist(filter_name)
                filter_name += '__in'
                plants = plants.filter(**{filter_name: filter_values})
    print('!-----------------------!')
    print(time.time() - start)
    print('!-----------------------!')
    return plants, filters_min_max
