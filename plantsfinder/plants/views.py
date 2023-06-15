from django.shortcuts import get_object_or_404, render

from plants.filters.filter_plants import filter_plants
from plants.models import Deciduous
from utils.get_text.plant_info import (get_plant_name,
                                       get_plant_usda_zones_min_max,
                                       get_plant_sun_types,
                                       get_plant_soil_types,
                                       get_plant_soil_ph_min_max,
                                       get_plant_soil_moisture)
from utils.pagination.pagination import get_pagination
from utils.query.string import delete_page_from_query_string

PLANTS_TYPES = {
    'deciduous': Deciduous,
    # 'coniferous': Coniferous,
    # 'herbaceous': Herbaceous,
}

PLANTS_PER_PAGE = 24


def plants_list(request, category):
    """Страницы подбора рестений."""
    template = 'plants/finder.html'
    filters = request.GET
    plant_type_model = PLANTS_TYPES[category]
    category_verbose_name = plant_type_model._meta.verbose_name_plural.title()
    plants = plant_type_model.objects.all()
    filters_min_max = {}
    if filters:
        plants, filters_min_max = filter_plants(plants, filters)
    page_obj, pagination = get_pagination(request, plants, PLANTS_PER_PAGE)
    context = {
        'request': request,
        'plant_category': category,
        'category_verbose_name': category_verbose_name,
        'plants': page_obj,
        'fields': plant_type_model.fields,
        'filters': filters_min_max,
        'pagination': pagination,
        'query_string': delete_page_from_query_string(request),
    }
    return render(request, template, context)


def plant_info(request, category, plant_slug):
    """Страницы с информацией о растении."""
    template = 'plants/plant_info.html'
    plant = get_object_or_404(PLANTS_TYPES[category], slug=plant_slug)
    context = {
        'request': request,
        'category': PLANTS_TYPES[category],
        'plant': plant,
        'plant_name': get_plant_name(plant),
        'usda_zones_min_max': get_plant_usda_zones_min_max(plant),
        'sun': get_plant_sun_types(plant),
        'soil': get_plant_soil_types(plant),
        'soil_ph': get_plant_soil_ph_min_max(plant),
        'soil_moisture': get_plant_soil_moisture(plant),
    }
    return render(request, template, context)