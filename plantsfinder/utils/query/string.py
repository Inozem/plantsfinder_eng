def delete_page_from_query_string(request):
    """
    Returns the query string without a page number.
    """
    query_string = request.META['QUERY_STRING']
    if query_string:
        query_list = query_string.split('&')
        query_string = '?'
        for query in query_list:
            if 'page=' not in query:
                query_string += query + '&'
    else:
        query_string = '?'
    return query_string
