from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline

from .models import Order
from .models import ProductInOrder
from .models import Status


class ProductInOrderInline(admin.TabularInline):
    model = ProductInOrder


class OrderAdmin(admin.ModelAdmin):
    inlines = [ProductInOrderInline, ]


admin.site.register(Order, OrderAdmin)
admin.site.register(ProductInOrder)
admin.site.register(Status)
