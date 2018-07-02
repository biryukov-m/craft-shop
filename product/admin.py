from django.contrib import admin


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

from .models import ShirtImage
from .models import ShirtPatternImage
from .models import TShirtImage
from .models import TShirtPatternImage
from .models import DressImage
from .models import DressPatternImage
from .models import TunicImage
from .models import TunicPatternImage
from .models import SkirtImage
from .models import SkirtPatternImage
from .models import BagImage
from .models import CosmeticBagImage
from .models import MobileCaseImage
from .models import TableClothImage


#  Абстрактная (де-факто) админ-модель для вещей
class ClothesAdmin(admin.ModelAdmin):
    list_display = ["name", "brand", "price", "created"]
    list_filter = ["brand", "gender", "fabric", "color", "created"]
    search_fields = ["name"]


# Админка для сорочки
# class ShirtImageInline(admin.TabularInline):
#     model = ShirtImage
#     extra = 3


class ShirtAdmin(ClothesAdmin):
    # inlines = [ShirtImageInline]
    pass


admin.site.register(Shirt, ShirtAdmin)


# Админка для заготовки сорочки
# class ShirtPatternImageInline(admin.TabularInline):
#     model = ShirtPatternImage
#     extra = 3


class ShirtPatternAdmin(ClothesAdmin):
    # inlines = [ShirtPatternImageInline]
    pass


admin.site.register(ShirtPattern, ShirtPatternAdmin)


# Админка для футболки
# class TShirtImageInline(admin.TabularInline):
#     model = TShirtImage
#     extra = 3


class TShirtAdmin(ClothesAdmin):
    # inlines = [TShirtImageInline]
    pass


admin.site.register(TShirt, TShirtAdmin)


# Админка для заготовки футболки
# class TShirtPatternImageInline(admin.TabularInline):
#     model = TShirtPatternImage
#     extra = 3


class TShirtPatternAdmin(ClothesAdmin):
    # inlines = [TShirtPatternImageInline]
    pass


admin.site.register(TShirtPattern, TShirtPatternAdmin)


# Админка для спідниці
# class DressImageInline(admin.TabularInline):
#     model = DressImage
#     extra = 3


class DressAdmin(ClothesAdmin):
    # inlines = [DressImageInline]
    pass


admin.site.register(Dress, DressAdmin)


# Админка для заготовки спідниці
# class DressPatternImageInline(admin.TabularInline):
    # model = DressPatternImage
    # extra = 3


class DressPatternAdmin(ClothesAdmin):
    # inlines = [DressPatternImageInline]
    pass


admin.site.register(DressPattern, DressPatternAdmin)


# Админка для сукні
# class SkirtImageInline(admin.TabularInline):
    # model = SkirtImage
    # extra = 3


class SkirtAdmin(ClothesAdmin):
    # inlines = [SkirtImageInline]
    pass


admin.site.register(Skirt, SkirtAdmin)


# Админка для заготовки сукні
# class SkirtPatternImageInline(admin.TabularInline):
    # model = SkirtPatternImage
    # extra = 3


class SkirtPatternAdmin(ClothesAdmin):
    # inlines = [SkirtPatternImageInline]
    pass


admin.site.register(SkirtPattern, SkirtPatternAdmin)


# Админка для туніки
# class TunicImageInline(admin.TabularInline):
#     model = TunicImage
#     extra = 3


class TunicAdmin(ClothesAdmin):
    # inlines = [TunicImageInline]
    pass


admin.site.register(Tunic, TunicAdmin)


# Админка для заготовки туніки
# class TunicPatternImageInline(admin.TabularInline):
#     model = TunicPatternImage
#     extra = 3


class TunicPatternAdmin(ClothesAdmin):
    # inlines = [TunicPatternImageInline]
    pass


admin.site.register(TunicPattern, TunicPatternAdmin)


# Админка для сумки
# class BagImageInline(admin.TabularInline):
#     model = BagImage
#     extra = 3


class BagAdmin(admin.ModelAdmin):
    # inlines = [BagImageInline]
    pass


admin.site.register(Bag, BagAdmin)


# Админка для косметички
# class CosmeticBagImageInline(admin.TabularInline):
#     model = CosmeticBagImage
#     extra = 3


class CosmeticBagAdmin(admin.ModelAdmin):
    # inlines = [CosmeticBagImageInline]
    pass


admin.site.register(CosmeticBag, CosmeticBagAdmin)


# Админка для чохла для телефону
# class MobileCaseImageInline(admin.TabularInline):
#     model = MobileCaseImage
#     extra = 3


class MobileCaseAdmin(admin.ModelAdmin):
    # inlines = [MobileCaseImageInline]
    pass


admin.site.register(MobileCase, MobileCaseAdmin)


# Админка для сорочки
# class TableClothImageInline(admin.TabularInline):
#     model = TableClothImage
#     extra = 3


class TableClothAdmin(admin.ModelAdmin):
    # inlines = [TableClothImageInline]
    pass


admin.site.register(TableCloth, TableClothAdmin)
