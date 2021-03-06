from django.urls import path
from .views import Main
from .views import OrdersList
from .views import OrderDetail
from .views import OrderRemove
from .views import AllProducts
from .views import ProductDetail


urlpatterns = [
    path('', Main.as_view(), name='main'),
    path('orders/', OrdersList.as_view(), name='orders'),
    path('order/<int:order_code>', OrderDetail.as_view(), name='order'),
    path('order/<int:order_code>/remove', OrderRemove.as_view(), name='order_remove'),
    path('products/', AllProducts.as_view(), name='products'),
    path('product/<int:product_code>', ProductDetail.as_view(), name='product'),

]

app_name = 'custom_admin'
