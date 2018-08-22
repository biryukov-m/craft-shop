from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline

from .models import Department
from .models import Section
from .models import ItemType
from .models import Item
from .models import ItemImage


class ImageInline(GenericTabularInline):
    model = ItemImage


#  Абстрактная (де-факто) админ-модель для вещей
class ClothesAdmin(admin.ModelAdmin):
    list_display = ["name", "brand", "price", "created"]
    list_filter = ["brand", "gender", "fabric", "color", "created"]
    search_fields = ["name"]
    inlines = [
            ImageInline,
        ]

admin.site.register(Department)
admin.site.register(Section)
admin.site.register(ItemType)
admin.site.register(Item, ClothesAdmin)
