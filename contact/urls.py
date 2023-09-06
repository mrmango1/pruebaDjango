from django.urls import path
from . import views

urlpatterns = [
    path('',views.contact,name="contact"),# en esat url hay nque quitar services/
]