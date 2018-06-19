from django.contrib import admin
from main.models import Genders
from main.models import Brand
from main.models import Fabric
from main.models import Size
from main.models import Color

from main.models import Shirt
from main.models import ShirtPattern
from main.models import TShirt
from main.models import TShirtPattern
from main.models import Dress
from main.models import DressPattern
from main.models import Tunic
from main.models import TunicPattern
from main.models import Skirt
from main.models import SkirtPattern
from main.models import Bag
from main.models import CosmeticBag
from main.models import MobileCase
from main.models import TableCloth



# Register your models here.
#
# admin.site.register(Genders)
# admin.site.register(Brand)
# admin.site.register(Fabric)
# admin.site.register(Size)
# admin.site.register(Color)
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

