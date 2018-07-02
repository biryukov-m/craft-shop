import os
from django.db import models
from properties import models as properties
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


def get_upload_path(instance, filename):
    return os.path.join(
        'item_images',
        "{}".format(instance.content_type.model),
        "{}".format(instance.object_id),
        filename
    )


# Абстрактный класс для единицы товара
class Item(models.Model):
    # code = models.PositiveIntegerField(default=None, blank=True, verbose_name="код", unique=True, editable=False)
    name = models.CharField(default=None, blank=True, verbose_name='найменування', max_length=40)
    description = models.TextField(default=None, verbose_name='опис', max_length=3000)
    price = models.IntegerField(default=None, blank=True, verbose_name='ціна')
    available = models.BooleanField(default=False, verbose_name='у продажі')
    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='додано')
    updated = models.DateTimeField(auto_now=True, auto_now_add=False, verbose_name='редаговано')
    item_code = models.CharField(default=None, blank=True, max_length=20)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


# Абстрактный класс для элементов одежды
class Clothes(Item):
    gender = models.ForeignKey(properties.Gender, on_delete=models.PROTECT, verbose_name="стать")
    brand = models.ForeignKey(properties.Brand, on_delete=models.PROTECT, verbose_name="виробник")
    fabric = models.ForeignKey(properties.Fabric, on_delete=models.PROTECT, verbose_name="тканина")
    color = models.ForeignKey(properties.Color, on_delete=models.PROTECT, verbose_name="колір")
    size = models.ForeignKey(properties.Size, on_delete=models.PROTECT, verbose_name="розмір")

    class Meta:
        abstract = True


# Абстрактный класс для заготовок
class Pattern(models.Model):
    partial = models.BooleanField(default=False, verbose_name="з відрізами")
    sleeve_length = models.IntegerField(default=None, blank=True, verbose_name="довжина рукава")
    sleeve_width = models.IntegerField(default=None, blank=True, verbose_name="ширина рукава")
    body_length = models.IntegerField(default=None, blank=True, verbose_name="довжина основи")
    body_width = models.IntegerField(default=None, blank=True, verbose_name="ширина основи")

    class Meta:
        abstract = True
        verbose_name = "заготовка"
        verbose_name_plural = "заготовки"


# Абстрактный класс для изображений товаров
class ItemImage(models.Model):
    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='додано')
    updated = models.DateTimeField(auto_now=True, auto_now_add=False, verbose_name='редаговано')

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    product_object = GenericForeignKey('content_type', 'object_id')

    is_active = models.BooleanField(default=True, verbose_name='показувати')
    is_basic = models.BooleanField(default=False, verbose_name='основне фото')

    image = models.ImageField(default=None,
                              blank=True,
                              verbose_name='фото товару',
                              upload_to=get_upload_path)

    def __str__(self):
        return "Изображение для {}".format(self.content_type.model)

    class Meta:
        verbose_name = "Зображення товару"
        verbose_name_plural = "Зображення товарів"


# Сорочка
class Shirt(Clothes):

    class Meta:
        verbose_name = "сорочка"
        verbose_name_plural = "сорочки"


# Заготовка сорочки
class ShirtPattern(Clothes, Pattern):

    class Meta:
        verbose_name = "заготовка сорочки"
        verbose_name_plural = "заготовки сорочок"


# Футболка
class TShirt(Clothes):

    class Meta:
        verbose_name = "футболка"
        verbose_name_plural = "футболки"


# Заготовка футболки
class TShirtPattern(Clothes, Pattern):

    class Meta:
        verbose_name = "заготовка футболки"
        verbose_name_plural = "заготовки футболок"


# Сукня
class Dress(Clothes):

    class Meta:
        verbose_name = "сукня"
        verbose_name_plural = "сукні"


# Заготовка сукні
class DressPattern(Clothes, Pattern):

    class Meta:
        verbose_name = "заготовка сукні"
        verbose_name_plural = "заготовки суконь"


# Туніка
class Tunic(Clothes):

    class Meta:
        verbose_name = "туніка"
        verbose_name_plural = "туніки"


# Заготовка туніки
class TunicPattern(Clothes, Pattern):

    class Meta:
        verbose_name = "заготовка туніки"
        verbose_name_plural = "заготовки тунік"


# Спідниця
class Skirt(Clothes):

    class Meta:
        verbose_name = "спідниця"
        verbose_name_plural = "спідниці"


# Заготовка спідниці
class SkirtPattern(Clothes, Pattern):

    class Meta:
        verbose_name = "заготовка спідниці"
        verbose_name_plural = "заготовки спідниць"


# Сумка
class Bag(Item):

    class Meta:
        verbose_name = "сумка"
        verbose_name_plural = "сумки"


# Косметичка
class CosmeticBag(Item):

    class Meta:
        verbose_name = "косметичка"
        verbose_name_plural = "косметички"


# Чохол для мобільного
class MobileCase(Item):

    class Meta:
        verbose_name = "чохол для мобільного телефону"
        verbose_name_plural = "чохли для мобільних телефонів"


# Скатертина
class TableCloth(Item):

    class Meta:
        verbose_name = "скатертина"
        verbose_name_plural = "скатертини"
