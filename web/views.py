from django.views.generic import TemplateView

from .models import Banner


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['banners'] = Banner.objects.all()
        print(context['banners'][0].image)
        return context
