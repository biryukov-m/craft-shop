import os
from django.db import models
from properties import models as properties
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


def get_upload_path(instance, filename):
    return os.path.join(
        'item_images',
        "{}".format(instance._meta.model_name),
        "{}".format(instance.item.item_code),
        filename
    )


# Абстрактный класс для единицы товара
class Item(models.Model):
    # code = models.PositiveIntegerField(default=None, blank=True, verbose_name="код", unique=True, editable=False)
    name = models.CharField(default=None, blank=True, verbose_name='найменування', max_length=40)
    description = models.TextField(default=None, verbose_name='описание', max_length=3000)
    price = models.IntegerField(default=None, blank=True, verbose_name='ціна')
    available = models.BooleanField(default=False, verbose_name='у продажі')
    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='додано')
    updated = models.DateTimeField(auto_now=True, auto_now_add=False, verbose_name='редаговано')
    item_code = models.CharField(default=None, blank=True, max_length=20)
    code = '000'

    class Meta:
        abstract = True

    def __str__(self):
        return self.name
    #
    # def save(self, *args, **kwargs):
        # self.code = int(100000 + int(self.pk))
        # print(type(self._get_pk_val))
        # super(Item, self).save(*args, **kwargs)
        # vasa = self.id
        # print(vasa)
        # print(type(vasa))


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


    # def __str__(self):
        # return "Изображение для {}".format(self.)

    class Meta:
        verbose_name = "Зображення товару"
        verbose_name_plural = "Зображення товарів"
        abstract = True


# Сорочка
class Shirt(Clothes):
    code = '001'

    class Meta:
        verbose_name = "сорочка"
        verbose_name_plural = "сорочки"


# class ShirtImage(ItemImage):
#     image = models.ImageField(default=None,
#                               blank=True,
#                               verbose_name='фото товару',
#                               upload_to=get_upload_path)
#     item = models.ForeignKey(Shirt, on_delete=models.CASCADE, verbose_name='товар')


# Заготовка сорочки
class ShirtPattern(Clothes, Pattern):
    code = '002'

    class Meta:
        verbose_name = "заготовка сорочки"
        verbose_name_plural = "заготовки сорочок"


# class ShirtPatternImage(ItemImage):
#     image = models.ImageField(default=None,
#                               blank=True,
#                               verbose_name='фото товару',
#                               upload_to='item_images/shirt_pattern_images')
#     item = models.ForeignKey(ShirtPattern, on_delete=models.CASCADE, verbose_name='товар')


# Футболка
class TShirt(Clothes):
    code = '003'

    class Meta:
        verbose_name = "футболка"
        verbose_name_plural = "футболки"


# class TShirtImage(ItemImage):
#     image = models.ImageField(default=None,
#                               blank=True,
#                               verbose_name='фото товару',
#                               upload_to='item_images/tshirt_images')
#     item = models.ForeignKey(TShirt, on_delete=models.CASCADE, verbose_name='товар')


# Заготовка футболки
class TShirtPattern(Clothes, Pattern):
    code = '004'

    class Meta:
        verbose_name = "заготовка футболки"
        verbose_name_plural = "заготовки футболок"


# class TShirtPatternImage(ItemImage):
#     image = models.ImageField(default=None,
#                               blank=True,
#                               verbose_name='фото товару',
#                               upload_to='item_images/tshirt_pattern_images')
#     item = models.ForeignKey(TShirtPattern, on_delete=models.CASCADE, verbose_name='товар')


# Сукня
class Dress(Clothes):
    code = '005'

    class Meta:
        verbose_name = "сукня"
        verbose_name_plural = "сукні"


# class DressImage(ItemImage):
#     image = models.ImageField(default=None,
#                               blank=True,
#                               verbose_name='фото товару',
#                               upload_to='item_images/dress_images')
#     item = models.ForeignKey(Dress, on_delete=models.CASCADE, verbose_name='товар')


# Заготовка сукні
class DressPattern(Clothes, Pattern):
    code = '006'

    class Meta:
        verbose_name = "заготовка сукні"
        verbose_name_plural = "заготовки суконь"


# class DressPatternImage(ItemImage):
#     image = models.ImageField(default=None,
#                               blank=True,
#                               verbose_name='фото товару',
#                               upload_to='item_images/dress_pattern_images')
#     item = models.ForeignKey(DressPattern, on_delete=models.CASCADE, verbose_name='товар')


# Туніка
class Tunic(Clothes):
    code = '007'

    class Meta:
        verbose_name = "туніка"
        verbose_name_plural = "туніки"


# class TunicImage(ItemImage):
#     image = models.ImageField(default=None,
#                               blank=True,
#                               verbose_name='фото товару',
#                               upload_to='item_images/tunic_images')
#     item = models.ForeignKey(Tunic, on_delete=models.CASCADE, verbose_name='товар')


# Заготовка туніки
class TunicPattern(Clothes, Pattern):
    code = '008'

    class Meta:
        verbose_name = "заготовка туніки"
        verbose_name_plural = "заготовки тунік"


# class TunicPatternImage(ItemImage):
#     image = models.ImageField(default=None,
#                               blank=True,
#                               verbose_name='фото товару',
#                               upload_to='item_images/tunic_pattern_images')
#     item = models.ForeignKey(TunicPattern, on_delete=models.CASCADE, verbose_name='товар')


# Спідниця
class Skirt(Clothes):
    code = '009'

    class Meta:
        verbose_name = "спідниця"
        verbose_name_plural = "спідниці"


# class SkirtImage(ItemImage):
#     image = models.ImageField(default=None,
#                               blank=True,
#                               verbose_name='фото товару',
#                               upload_to='item_images/skirt_images')
#     item = models.ForeignKey(Skirt, on_delete=models.CASCADE, verbose_name='товар')


# Заготовка спідниці
class SkirtPattern(Clothes, Pattern):
    code = '010'

    class Meta:
        verbose_name = "заготовка спідниці"
        verbose_name_plural = "заготовки спідниць"


# class SkirtPatternImage(ItemImage):
#     image = models.ImageField(default=None,
#                               blank=True,
#                               verbose_name='фото товару',
#                               upload_to='item_images/skirt_pattern_images')
#     item = models.ForeignKey(SkirtPattern, on_delete=models.CASCADE, verbose_name='товар')


# Аксессуари


# Сумка
class Bag(Item):
    code = '011'

    class Meta:
        verbose_name = "сумка"
        verbose_name_plural = "сумки"


# class BagImage(ItemImage):
#     image = models.ImageField(default=None,
#                               blank=True,
#                               verbose_name='фото товару',
#                               upload_to='item_images/bag_images')
#     item = models.ForeignKey(Bag, on_delete=models.CASCADE, verbose_name='товар')


# Косметичка
class CosmeticBag(Item):
    code = '012'

    class Meta:
        verbose_name = "косметичка"
        verbose_name_plural = "косметички"


# class CosmeticBagImage(ItemImage):
#     image = models.ImageField(default=None,
#                               blank=True,
#                               verbose_name='фото товару',
#                               upload_to='item_images/cosmetic_bag_images')
#     item = models.ForeignKey(CosmeticBag, on_delete=models.CASCADE, verbose_name='товар')


# Чохол для мобільного
class MobileCase(Item):
    code = '013'

    class Meta:
        verbose_name = "чохол для мобільного телефону"
        verbose_name_plural = "чохли для мобільних телефонів"


# class MobileCaseImage(ItemImage):
#     image = models.ImageField(default=None,
#                               blank=True,
#                               verbose_name='фото товару',
#                               upload_to='item_images/mobile_case_images')
#     item = models.ForeignKey(MobileCase, on_delete=models.CASCADE, verbose_name='товар')


# Скатертина
class TableCloth(Item):
    code = '014'

    class Meta:
        verbose_name = "скатертина"
        verbose_name_plural = "скатертини"


# class TableClothImage(ItemImage):
#     image = models.ImageField(default=None,
#                               blank=True,
#                               verbose_name='фото товару',
#                               upload_to='item_images/table_cloth_images')
#     item = models.ForeignKey(TableCloth, on_delete=models.CASCADE, verbose_name='товар')
