from django.urls import path
from product.views import index
from django.contrib import admin


admin.autodiscover()

urlpatterns = [
    path('', index, name='Index')
]
