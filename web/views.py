from django.views.generic import TemplateView

from .models import Banner, Member


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['banners'] = Banner.objects.all()
        context['is_sub'] = False
        return context


class Subpage(TemplateView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_sub'] = True
        return context


class ContactView(Subpage):
    template_name = 'contact.html'


class MembersView(Subpage):
    template_name = 'members.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['members'] = Member.objects.all()
        return context


class AboutView(Subpage):
    template_name = 'about.html'


class ProjectsView(Subpage):
    template_name = 'projects.html'
