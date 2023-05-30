from django.urls import path
from . import views

urlpatterns = [
    path("", views.api_home, name="home"),
    # path('api/', apiOverview, name="api-overview"),
]
