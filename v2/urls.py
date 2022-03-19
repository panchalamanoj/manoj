from django.contrib import admin
from . immport views

urlpatterns = [
    path('', views.index, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
]    


