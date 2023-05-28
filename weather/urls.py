from django.urls import path

from backend.views import MainView

urlpatterns = [
    path("main/<str:name>", MainView.as_view(), name="main"),
]
