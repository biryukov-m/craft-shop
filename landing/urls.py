from django.urls import path
from .views import home
from django.contrib import admin

urlpatterns = [
    # path('', index, name='Index')
    path('', home)
]
