from django.urls import path

from backend.views import MainView

urlpatterns = [
       path('main/', MainView.as_view(), name='main-main'),
]
