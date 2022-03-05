from django.urls import URLPattern, path
from . import views

URLPattern = [
    path("", views.login,name="login")
]