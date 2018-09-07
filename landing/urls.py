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
    path('shop/<slug:department_slug>', department, name='department'),
    path('shop/<slug:department_slug>/<slug:section_slug>', section, name='section'),
    path('shop/<slug:department_slug>/<slug:section_slug>/<slug:item_type_slug>', item_type, name='item_type'),
    path('shop/<slug:department_slug>/<slug:section_slug>/<slug:item_type_slug>/<slug:item_slug>', item, name='item'),
    path('', home)
]

app_name = 'landing'
