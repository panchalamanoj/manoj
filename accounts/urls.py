from django.urls import path
from . import views

URLPattern = [
    path("", views.register,name="register")
]
