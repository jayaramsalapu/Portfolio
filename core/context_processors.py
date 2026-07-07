from .models import Profile

def profile_context(request):
    """
    Injects the user's Profile into the context of all templates.
    """
    return {
        'profile': Profile.objects.first()
    }
