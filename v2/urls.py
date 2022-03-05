from django.urls import URLPattern, path
from . import views

URLPattern = [
    path("", views.register,name="register")
]
