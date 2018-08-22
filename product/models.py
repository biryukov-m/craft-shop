import os
from django.db import models
from properties import models as properties
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from eav.decorators import register_eav


def get_upload_path(instance, filename):
    return os.path.join(
        'item_images',
        "{}".format(instance.content_type.model),
        "{}".format(instance.object_id),
        filename
    )


class Department(models.Model):
    name = models.CharField(default=None, max_length=100, verbose_name="назва відділу")
    code_name = models.CharField(default=None, max_length=100, verbose_name="програмна назва")
    notes = models.TextField(default=None, blank=True, max_length=2000, verbose_name="примітки")

    class Meta:
        verbose_name = "відділ магазину"
        verbose_name_plural = "відділи магазину"

    def __str__(self):
        return self.name


class Section(models.Model):
    name = models.CharField(default=None, max_length=100, verbose_name="назва")
    code_name = models.CharField(default=None, max_length=100, verbose_name="програмна назва")
    notes = models.TextField(default=None, blank=True, max_length=2000, verbose_name="примітки")
    department = models.ForeignKey(Department, on_delete=models.DO_NOTHING, default=None, verbose_name="відділ магазину")

    class Meta:
        verbose_name = "секція відділу магазину"
        verbose_name_plural = "секції відділів магазину"

    def __str__(self):
        return self.name


class ItemType(models.Model):
    name = models.CharField(default=None, max_length=100, verbose_name="назва типу товару")
    name_plural = models.CharField(default=None, max_length=100, verbose_name="назва типу товару у множині")
    code_name = models.CharField(default=None, max_length=100, verbose_name="програмна назва")
    notes = models.TextField(default=None, blank=True, max_length=2000, verbose_name="примітки")
    section = models.ForeignKey(Section, on_delete=models.DO_NOTHING, default=None, verbose_name="секція магазину")

    class Meta:
        verbose_name = "тип товару"
        verbose_name_plural = "типи товарів"

    def __str__(self):
        return "{} ({})".format(self.name, self.section)


# Абстрактный класс для единицы товара
@register_eav()
class Item(models.Model):
    code = models.PositiveIntegerField(default=None, blank=True, verbose_name="код", unique=True, editable=False)
    name = models.CharField(default=None,
                            blank=True,
                            verbose_name='найменування',
                            max_length=40)

    item_type = models.ForeignKey(ItemType, verbose_name="тип товару", on_delete=models.DO_NOTHING)

    description = models.TextField(default=None,
                                   verbose_name='опис',
                                   max_length=3000)

    price = models.DecimalField(default=None,
                                blank=True,
                                decimal_places=2,
                                max_digits=10,
                                verbose_name='ціна')

    available = models.BooleanField(default=False,
                                    verbose_name='у продажі')

    created = models.DateTimeField(auto_now_add=True,
                                   auto_now=False,
                                   verbose_name='додано')

    updated = models.DateTimeField(auto_now=True,
                                   auto_now_add=False,
                                   verbose_name='редаговано')

    item_code = models.CharField(default=None,
                                 blank=True,
                                 max_length=20)

    gender = models.ForeignKey(properties.Gender, on_delete=models.PROTECT, verbose_name="стать")
    brand = models.ForeignKey(properties.Brand, on_delete=models.PROTECT, verbose_name="виробник")
    fabric = models.ForeignKey(properties.Fabric, on_delete=models.PROTECT, verbose_name="тканина")
    color = models.ForeignKey(properties.Color, on_delete=models.PROTECT, verbose_name="колір")
    size = models.ForeignKey(properties.Size, on_delete=models.PROTECT, verbose_name="розмір")

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товари"

    def __str__(self):
        return "{} - {}".format(self.name, self.price)


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
