from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('change_password', views.change_password, name='change_password'),

    path('access_denied', views.access_denied, name='access_denied'),

    path('email_validation', views.email_validation, name='email_validation'),
    path('old_password_validation', views.old_password_validation, name='old_password_validation'),
    path('new_password_validation', views.new_password_validation, name='new_password_validation'),

    path('miembros', views.miembros, name='miembros'),
    path('agregar_miembro', views.agregar_miembro, name='agregar_miembro'),
    path('editar_miembro/<int:primary_key>', views.editar_miembro, name='editar_miembro'),
    path('eliminar_miembro/<int:primary_key>', views.eliminar_miembro, name='eliminar_miembro'),

    path('misiones', views.misiones, name='misiones'),
    path('agregar_mision', views.agregar_mision, name='agregar_mision'),
    path('editar_mision/<int:primary_key>', views.editar_mision, name='editar_mision'),
    path('eliminar_mision/<int:primary_key>', views.eliminar_mision, name='eliminar_mision'),

    path('subsistemas', views.subsistemas, name='subsistemas'),
    path('agregar_subsistema', views.agregar_subsistema, name='agregar_subsistema'),
    path('editar_subsistema/<int:primary_key>', views.editar_subsistema, name='editar_subsistema'),
    path('eliminar_subsistema/<int:primary_key>', views.eliminar_subsistema, name='eliminar_subsistema'),

    path('view_image/<path:image_url>', views.view_image, name='view_image'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
