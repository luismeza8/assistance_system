from .models import Miembro
from django.shortcuts import redirect


def admin_role_required(func):
    def wrapper(request):
        if request.user.role == Miembro.ROLES['A']:
            return func(request)
        else:
            return redirect('access_denied')
    return wrapper
