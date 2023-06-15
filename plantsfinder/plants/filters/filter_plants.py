from django.db.models import Max, Min


def filter_plants(plants, filters):
    """
    Фильтрация растений в соответствии с запросом и
    создание переменной с минимальными и максимальными значениями фильтров
    (если они были в запросе).
    """
    filters_min_max = {}
    for filter_name in filters:
        if (('-min' in filter_name or '-max' in filter_name)
                and (filters[filter_name] != '')):
            filter_suffixes = {
                '-min': '__lt',
                '-max': '__gt',
            }
            if 'soil_ph' in filter_name:
                if '-max' in filter_name:
                    plants = plants.annotate(soil_ph_min=Min('soil_ph__name'))
                    filter_suffixes['-max'] = '_min__gt'
                elif '-min' in filter_name:
                    plants = plants.annotate(soil_ph_max=Max('soil_ph__name'))
                    filter_suffixes['-min'] = '_max__lt'
            suffix = filter_name[-4:]
            new_suffix = filter_suffixes[suffix]
            filter_name_compare = filter_name.replace(suffix, new_suffix)
            filter_value = float(filters[filter_name])
            plants = plants.exclude(**{filter_name_compare: filter_value})
            filters_min_max[filter_name] = filters[filter_name]
        elif filter_name not in ('page', ) and filters[filter_name] != '':
            filter_values = filters.getlist(filter_name)
            filter_name += '__in'
            plants = plants.filter(**{filter_name: filter_values})
    return plants, filters_min_max
