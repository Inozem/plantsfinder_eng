from django.db import models
from django.db.models import Max, Min
from django.shortcuts import get_object_or_404

FIELDS_ORDER = ['usda_zone', 'sun', 'soil_moisture', 'soil_type',
                'soil_fertility', 'soil_ph', 'plant_type',
                'foliage_type_deciduous', 'max_height', 'max_width',
                'leaf_color', 'leaf_color_change', 'young_leaf_color',
                'autumn_leaf_color', 'flowering_color', 'flowering_period',
                'scent', 'bark_color', 'fruit_color', 'other_plant_features',
                'hazardous']
FIELDS_MIN_MAX = ('max_height', 'max_width', 'soil_ph')


def sort_plant_fields(plant_fields):
    """
    Returns a dictionary with field assignments and
    their models that are needed to be displayed on the plant selection page.
    """
    sorted_fields = {}
    for field in FIELDS_ORDER:
        if field in plant_fields:
            sorted_fields[field] = plant_fields[field]
    return sorted_fields


def get_plant_class_fields(plant_class, PlantInfo):
    """
    Returns dictionary with names of fields
    that should be on the web page and their models.
    """
    fields_comparison = {
        plant_class._meta.fields: PlantInfo._meta.fields,
        plant_class._meta.many_to_many: PlantInfo._meta.many_to_many,
    }
    plant_fields = {}
    for fields, unnecessary_fields in fields_comparison.items():
        for field in fields:
            if field not in unnecessary_fields and '_ptr' not in field.name:
                plant_fields[field.name] = field
    return {**sort_plant_fields(plant_fields)}


def collect_values(plant_class, fields_and_names):
    """
    Collects field names and lists of their values (or id values).
    And return a dictionary with this data.
    """
    field_values = {}
    plants = plant_class.objects.all()
    for required_field_name in fields_and_names:
        for field_name_value in plants.values(required_field_name):
            for field_name, field_value in field_name_value.items():
                if field_value is not None:
                    if field_name not in field_values:
                        field_values[field_name] = [field_value]
                    elif field_value not in field_values[field_name]:
                        field_values[field_name] += [field_value]
    return field_values


def add_values(plant_class, field_values, fields_and_names, field_name):
    """
    Converts the list of values or id into a dictionary
    with the addition of values (if there was an id).
    """
    ids_and_values = {}

    for value in field_values:
        id = value
        if field_name in FIELDS_MIN_MAX:
            field_name_min_max = field_name
            field_m2m_model = fields_and_names[field_name]
            if isinstance(field_m2m_model, models.ManyToManyField):
                field_name_min_max += '__name'
            min_value = plant_class.objects.aggregate(Min(field_name_min_max))
            max_value = plant_class.objects.aggregate(Max(field_name_min_max))
            field_name_min = field_name_min_max + '__min'
            field_name_max = field_name_min_max + '__max'
            ids_and_values['min'] = str(min_value[field_name_min])
            ids_and_values['max'] = str(max_value[field_name_max])
            break
        elif isinstance(value, int):
            field_related_model = fields_and_names[field_name].related_model
            value = get_object_or_404(field_related_model, pk=value).name
        ids_and_values[str(id)] = value
    return ids_and_values


def get_fields_with_values(plant_class, PlantInfo):
    """
    Returns the necessary fields required for display
    on the plant selection page
    only with the values that are used in this class in the format:
    {
        <verbose_name>: {
            'field_related_name': <related_name>,
            'values': {<id_or_value>: <value>, ...},
        },
        ...,
    }

    For the subsequent transformation of this data into
    the fields of plant filters in template.
    """
    fields_and_names = get_plant_class_fields(plant_class, PlantInfo)
    fields_names_and_values = collect_values(plant_class, fields_and_names)
    plant_class_fields = {}
    for field_name, field_values in fields_names_and_values.items():
        field_values.sort()
        ids_and_values = add_values(plant_class, field_values,
                                    fields_and_names, field_name)
        field_verbose_name = fields_and_names[field_name].verbose_name.title()
        field_verbose_name = field_verbose_name.capitalize()
        plant_class_fields[field_verbose_name] = {
            'field_related_name': field_name,
            'values': ids_and_values
        }
    return plant_class_fields


def check_and_get_fields_presence(plants, plant_class, PlantInfo):
    """
    Checks for the presence of fields plant class and returns fields.
    """
    if len(plants) > 0 and len(plant_class.fields) == 0:
        plant_class.fields = get_fields_with_values(plant_class, PlantInfo)
    return plant_class.fields
