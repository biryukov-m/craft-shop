from django.urls import path
from orders.views import basket_add
from orders.views import basket_remove
from orders.views import checkout

urlpatterns = [
    path('basket_add/', basket_add, name='basket_add'),
    path('basket_remove/', basket_remove, name='basket_remove'),
    path('checkout/', checkout, name='checkout'),
]

app_name = 'orders'
