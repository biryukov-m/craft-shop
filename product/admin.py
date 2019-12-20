from django.contrib import admin
from django.contrib.admin import TabularInline
from django.contrib.admin import ModelAdmin
from django.forms import ModelForm

from .models import Department
from .models import Section
from .models import ItemType
from .models import Item
from .models import ItemImage


admin.site.register(Department)
admin.site.register(Section)
admin.site.register(ItemType)


class ImageInline(TabularInline):
    model = ItemImage


class ItemAdminForm(ModelForm):
    model = Item


class ItemAdmin(ModelAdmin):
    form = ItemAdminForm
    list_display = ["name", "item_type", "brand", "price", "created"]
    list_filter = ["brand", "item_type", "fabric", "color", "created"]
    search_fields = ["name"]
    inlines = [
        ImageInline,
    ]


admin.site.register(Item, ItemAdmin)
