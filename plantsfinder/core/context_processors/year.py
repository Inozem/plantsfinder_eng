from django.utils import timezone

now = timezone.now()


def year(request):
    """Returns current year."""
    return {
        'year': timezone.now().year
    }
