from django.contrib import admin
from product.models import Genders
from product.models import Brand
from product.models import Fabric
from product.models import Size
from product.models import Color

from product.models import Shirt
from product.models import ShirtPattern
from product.models import TShirt
from product.models import TShirtPattern
from product.models import Dress
from product.models import DressPattern
from product.models import Tunic
from product.models import TunicPattern
from product.models import Skirt
from product.models import SkirtPattern
from product.models import Bag
from product.models import CosmeticBag
from product.models import MobileCase
from product.models import TableCloth


# Register your models here.
#
admin.site.register(Genders)
admin.site.register(Brand)
admin.site.register(Fabric)
admin.site.register(Size)
admin.site.register(Color)


admin.site.register(Shirt)
admin.site.register(ShirtPattern)
admin.site.register(TShirt)
admin.site.register(TShirtPattern)
admin.site.register(Dress)
admin.site.register(DressPattern)
admin.site.register(Tunic)
admin.site.register(TunicPattern)
admin.site.register(Skirt)
admin.site.register(SkirtPattern)
admin.site.register(Bag)
admin.site.register(CosmeticBag)
admin.site.register(MobileCase)
admin.site.register(TableCloth)

