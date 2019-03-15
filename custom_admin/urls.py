from django.urls import path
from .views import Main
from .views import OrdersList
from .views import OrderDetail


urlpatterns = [
    path('', Main.as_view(), name='main'),
    path('orders/', OrdersList.as_view(), name='orders'),
    path('order/<int:order_code>', OrderDetail.as_view(), name='order'),
]

app_name = 'custom_admin'
