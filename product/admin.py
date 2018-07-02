from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline

from .models import Shirt
from .models import ShirtPattern
from .models import TShirt
from .models import TShirtPattern
from .models import Dress
from .models import DressPattern
from .models import Tunic
from .models import TunicPattern
from .models import Skirt
from .models import SkirtPattern
from .models import Bag
from .models import CosmeticBag
from .models import MobileCase
from .models import TableCloth
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

admin.site.register(Shirt, ClothesAdmin)
admin.site.register(ShirtPattern, ClothesAdmin)
admin.site.register(TShirt, ClothesAdmin)
admin.site.register(TShirtPattern, ClothesAdmin)
admin.site.register(Dress, ClothesAdmin)
admin.site.register(DressPattern, ClothesAdmin)
admin.site.register(Skirt, ClothesAdmin)
admin.site.register(SkirtPattern, ClothesAdmin)
admin.site.register(Tunic, ClothesAdmin)
admin.site.register(TunicPattern, ClothesAdmin)


class AccessoryAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "created"]
    list_filter = ["created"]
    search_fields = ["name"]
    inlines = [
            ImageInline,
        ]

admin.site.register(Bag, AccessoryAdmin)
admin.site.register(CosmeticBag, AccessoryAdmin)
admin.site.register(MobileCase, AccessoryAdmin)
admin.site.register(TableCloth, AccessoryAdmin)
