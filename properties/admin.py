from django.contrib import admin

from .models import Brand
from .models import Fabric
from .models import Size
from .models import Color
# Register your models here.

admin.site.register(Brand)
admin.site.register(Fabric)
admin.site.register(Size)
admin.site.register(Color)