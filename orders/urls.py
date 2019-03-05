from django.urls import path
from orders.views import basket_add
from orders.views import basket_remove
from orders.views import basket_change_quantity
from orders.views import checkout
from orders.views import checkout_success
from orders.views import single_order
from orders.views import GenerateOrderPdf

urlpatterns = [
    path('basket_add/', basket_add, name='basket_add'),
    path('basket_remove/', basket_remove, name='basket_remove'),
    path('basket_change_quantity/', basket_change_quantity, name='basket_change_quantity'),
    path('checkout/success/', checkout_success, name='checkout_success'),
    path('checkout/', checkout, name='checkout'),
    path('order/<int:code>/pdf/', GenerateOrderPdf.as_view(), name='order-pdf'),
    path('order/<int:code>/', single_order, name='single_order_code'),
    path('order/', single_order, name='single_order_hash_code'),

]

app_name = 'orders'
