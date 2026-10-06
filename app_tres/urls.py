from django.urls import path
from . import views

urlpatterns = [
    path('', views.vista_tres, name='vista_tres'),
]