from django.urls import path
from . import views

urlpattern = [
    path("", views.register,name="register")
]
