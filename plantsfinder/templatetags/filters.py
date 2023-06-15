from django import template

register = template.Library()


@register.filter
def get_value_list(dictionary, key):
    return dictionary.getlist(key)


@register.filter
def get_value_from_dict(dict_data, key):
    if key:
        return dict_data.get(key)