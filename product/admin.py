from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline

# from .models import Shirt
# from .models import ShirtPattern
# from .models import TShirt
# from .models import TShirtPattern
# from .models import Dress
# from .models import DressPattern
# from .models import Tunic
# from .models import TunicPattern
# from .models import Skirt
# from .models import SkirtPattern
# from .models import Bag
# from .models import CosmeticBag
# from .models import MobileCase
# from .models import TableCloth
from .models import ItemImage
from .models import Item
from .models import ItemType


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

admin.site.register(Item, ClothesAdmin)
admin.site.register(ItemType)
