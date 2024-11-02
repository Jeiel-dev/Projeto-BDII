from django.contrib import admin
from django.urls import path
from .views import login_user, register_user

urlpatterns = [
    path('', login_user, name='logar'),
    path('register/', register_user, name='register')
]
