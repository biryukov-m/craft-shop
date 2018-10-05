from django.urls import path
from .views import home
from .views import shop
from .views import section
from .views import department
from .views import ViewByItemType
from .views import ViewSingleItem

from django.contrib import admin

urlpatterns = [
    # path('', index, name='Index')
    path('shop/', shop, name='shop'),
    path('shop/<slug:department_slug>/', department, name='department'),
    path('shop/<slug:department_slug>/<slug:section_slug>', section, name='section'),
    path('shop/<slug:department_slug>/<slug:section_slug>/<slug:item_type_slug>', ViewByItemType.as_view(), name='item_type'),
    path('shop/<slug:department_slug>/<slug:section_slug>/<slug:item_type_slug>/<slug:item_slug>', ViewSingleItem.as_view(), name='item'),
    path('', home, name='home'),
]

app_name = 'landing'
