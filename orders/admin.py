from django.contrib import admin
from .models import Order
from .models import ProductInOrder

admin.site.register(Order)
admin.site.register(ProductInOrder)

# Register your models here.
