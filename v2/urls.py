from django.urls import path
from v2 import views

urlpatterns = [
      path("register", views.register, name="register"),
      path("login", views.login, name="login"),
]
