from django.urls import path
from .views import main
from .views import Orders


urlpatterns = [
    path('', main, name='main'),
    path('orders/', Orders.as_view(), name='orders'),
]

app_name = 'custom_admin'
