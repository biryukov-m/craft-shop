from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline

from .models import Department
from .models import Section
from .models import ItemType
from .models import Item
from .models import ItemImage

from eav.forms import BaseDynamicEntityForm
from eav.admin import BaseEntityAdmin

admin.site.register(Department)
admin.site.register(Section)
admin.site.register(ItemType)


class ImageInline(GenericTabularInline):
    model = ItemImage


class ItemAdminForm(BaseDynamicEntityForm):
    model = Item


class ItemAdmin(BaseEntityAdmin):
    form = ItemAdminForm
    list_display = ["name", "item_type", "brand", "price", "created"]
    list_filter = ["brand", "item_type", "gender", "fabric", "color", "created"]
    search_fields = ["name"]
    inlines = [
        ImageInline,
    ]

admin.site.register(Item, ItemAdmin)
