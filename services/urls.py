from django.urls import path
from . import views

urlpatterns = [
    path('',views.services, name="services"),# en esat url hay nque quitar services/
    ]