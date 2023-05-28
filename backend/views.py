from django.http import HttpResponse
from django.views.generic import ListView


class MainView(ListView):
    def get_queryset(self):
        return []

    def render_to_response(self, context, **response_kwargs):
        return HttpResponse("")
