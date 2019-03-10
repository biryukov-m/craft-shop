from django.urls import path
from .views import main
from .views import orders


urlpatterns = [
    path('', main, name='main'),
    path('orders/', orders, name='orders'),
]

app_name = 'custom_admin'
