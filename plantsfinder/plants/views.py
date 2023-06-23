from django.shortcuts import render


def main_page(request):
    """Creates main page for plantsfinder."""
    template = 'main_page.html'
    return render(request, template)
