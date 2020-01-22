from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('proyectos', ProjectsView.as_view(), name='projects'),
    path('miembros', MembersView.as_view(), name='members'),
    path('acerca-de', AboutView.as_view(), name='about'),
    path('contacto', ContactView.as_view(), name='contact'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
