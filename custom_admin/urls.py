from django.urls import path
from .views import Orders
from .views import Main


urlpatterns = [
    path('', Main.as_view(), name='main'),
    path('orders/', Orders.as_view(), name='orders'),
]

app_name = 'custom_admin'
