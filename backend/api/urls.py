from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path("auth/", obtain_auth_token, name="api_token_auth"),
    path("", views.api_home, name="home"),
    # path('api/', apiOverview, name="api-overview"),
]
