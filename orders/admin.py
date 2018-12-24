from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline

from .models import Order
from .models import ProductInOrder
from .models import Status
from .models import ProductInBasket


class ProductInOrderInline(admin.TabularInline):
    model = ProductInBasket


class ProductInBasketInline(admin.TabularInline):
    model = ProductInOrder


class OrderAdmin(admin.ModelAdmin):
    inlines = [ProductInOrderInline, ProductInBasketInline]


admin.site.register(Order, OrderAdmin)
admin.site.register(ProductInOrder)
admin.site.register(Status)
admin.site.register(ProductInBasket)
