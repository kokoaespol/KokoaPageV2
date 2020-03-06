from django.views.generic import TemplateView

from .models import Banner, Member


NAVIGATION = {}
NAVIGATION['home'] = {
    'text': 'Inicio',
    'active': False,
    'url': '/',
}
NAVIGATION['projects'] = {
    'text': 'Proyectos',
    'active': False,
    'url': 'proyectos',
}
NAVIGATION['members'] = {
    'text': 'Miembros',
    'active': False,
    'url': 'miembros',
}
NAVIGATION['about'] = {
    'text': 'Sobre nosotros',
    'active': False,
    'url': 'acerca-de',
}
NAVIGATION['contact'] = {
    'text': 'Contactanos',
    'active': False,
    'url': 'contacto',
}


def deactive_routes():
    for v in NAVIGATION.values():
        v['active'] = False


class BaseView(TemplateView):
    def get_context_data(self, **kwargs):
        deactive_routes()
        context = super().get_context_data(**kwargs)
        context['nav'] = NAVIGATION
        return context


class IndexView(BaseView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['banners'] = Banner.objects.all()
        NAVIGATION['home']['active'] = True
        return context


class ContactView(BaseView):
    template_name = 'contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        NAVIGATION['contact']['active'] = True
        return context


class MembersView(BaseView):
    template_name = 'members.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['members'] = Member.objects.all()
        NAVIGATION['members']['active'] = True
        return context


class AboutView(BaseView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        NAVIGATION['about']['active'] = True
        return context


class ProjectsView(BaseView):
    template_name = 'projects.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        NAVIGATION['projects']['active'] = True
        return context
