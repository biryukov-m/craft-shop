from django.urls import path
from .views import home
from .views import shop
from .views import department
from .views import section
from .views import item_type
from .views import item
from django.contrib import admin

urlpatterns = [
    # path('', index, name='Index')
    path('shop/', shop, name='shop'),
    path('shop/<slug:slug>', department, name='department'),
    # path('shop/<slug:slug>/<slug:slug>', section, name='department'),
    # path('shop/<slug:slug>/<slug:slug>/<slug:slug>', item_type, name='department'),
    # path('shop/<slug:slug>/<slug:slug>/<slug:slug>/<slug:slug>', item, name='department'),
    path('', home)
]
