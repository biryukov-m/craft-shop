from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline

from .models import Order
# from .models import Status
from .models import ProductInBasket


class ProductInBasketInline(admin.TabularInline):
    model = ProductInBasket


class OrderAdmin(admin.ModelAdmin):
    inlines = []


admin.site.register(Order, OrderAdmin)
# admin.site.register(Status)
admin.site.register(ProductInBasket)
