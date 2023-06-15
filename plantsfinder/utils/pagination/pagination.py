from math import ceil


def get_pagination(request, objects, objects_per_page):
    """Пагинация."""
    page_number = request.GET.get('page')
    if not page_number:
        page_number = 1
    page_number = int(page_number)
    objs_count = len(objects)
    pages_count = ceil(objs_count / objects_per_page)
    if pages_count == 1:
        return objects, None
    if page_number > pages_count > 0:
        page_number = pages_count
    first_plant_ind = 0 + (page_number - 1) * objects_per_page
    page_objs = objects[first_plant_ind:first_plant_ind+objects_per_page]
    pagination = {'page_number': page_number, }
    if page_number > 1:
        pagination['first_page'] = 1
        if page_number > 2:
            pagination['previous_page'] = page_number - 1
            if page_number > 3:
                pagination['first_ellipsis'] = '...'
    if pages_count - page_number > 0:
        pagination['last_page'] = pages_count
        if pages_count - page_number > 1:
            pagination['next_page'] = page_number + 1
            if pages_count - page_number > 2:
                pagination['last_ellipsis'] = '...'
    return page_objs, pagination
