# principal/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.buscar_ci, name='index'),
]
