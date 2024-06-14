from .models import Miembro
from django.shortcuts import redirect


def admin_role_required(func):
    def wrapper(request, *args, **kwargs):
        if request.user.role == 'A':
            return func(request, *args, **kwargs)
        else:
            return redirect('access_denied')
    return wrapper
