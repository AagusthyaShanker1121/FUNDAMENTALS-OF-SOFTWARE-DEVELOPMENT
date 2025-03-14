from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', view=views.index, name='index'),
    path('home', view=views.home, name='home')
]