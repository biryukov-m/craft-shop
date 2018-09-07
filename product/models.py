import os
from django.db import models
from properties import models as properties
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import reverse
from eav.decorators import register_eav


def get_upload_path(instance, filename):
    return os.path.join(
        'item_images',
        "{}".format(instance.content_type.model),
        "{}".format(instance.object_id),
        filename
    )


def get_section_upload_path(instance, filename):
    return os.path.join(
        'sections_images',
        "{}".format(instance.slug),
        filename
    )


class Department(models.Model):
    name = models.CharField(default=None, max_length=100, verbose_name="назва відділу")
    code_name = models.CharField(default=None, max_length=100, verbose_name="програмна назва")
    notes = models.TextField(default=None, blank=True, max_length=2000, verbose_name="примітки")
    slug = models.SlugField(default=None, blank=True, null=True, max_length=30, verbose_name="URL в адресній стрічці броузера")

    class Meta:
        verbose_name = "відділ магазину"
        verbose_name_plural = "відділи магазину"

    def __str__(self):
        return self.name

    def get_sections(self):
        return self.section_set.all()

    def get_brands(self):
        secs = self.section_set.all()
        all_brands = properties.Brand.objects.count()
        brands = []
        for sec in secs:
            for item_type in sec.itemtype_set.all():
                for item in item_type.item_set.all():
                    if item.brand not in brands and brands.count != all_brands:
                        brands.append(item.brand)
                    else:
                        break
        return brands

    def get_absolute_url(self):
        return reverse('landing:department', kwargs={"department_slug": self.slug})


class Section(models.Model):
    name = models.CharField(default=None, max_length=100, verbose_name="назва")
    code_name = models.CharField(default=None, max_length=100, verbose_name="програмна назва")
    notes = models.TextField(default=None, blank=True, max_length=2000, verbose_name="примітки")
    department = models.ForeignKey(Department, on_delete=models.DO_NOTHING, default=None, verbose_name="відділ магазину")
    slug = models.SlugField(default=None, blank=True, null=True, max_length=30, verbose_name="URL в адресній стрічці броузера")
    image = models.ImageField(default=None, blank=True, null=True, verbose_name="зображення секції", upload_to=get_section_upload_path)

    class Meta:
        verbose_name = "секція відділу магазину"
        verbose_name_plural = "секції відділів магазину"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse(
            'landing:section',
            kwargs={
                "department_slug": self.department.slug,
                "section_slug": self.slug
            }
        )


class ItemType(models.Model):
    name = models.CharField(default=None, max_length=100, verbose_name="назва типу товару")
    name_plural = models.CharField(default=None, max_length=100, verbose_name="назва типу товару у множині")
    code_name = models.CharField(default=None, max_length=100, verbose_name="програмна назва")
    notes = models.TextField(default=None, blank=True, max_length=2000, verbose_name="примітки")
    section = models.ForeignKey(Section, on_delete=models.DO_NOTHING, default=None, verbose_name="секція магазину")
    slug = models.SlugField(default=None, blank=True, null=True, max_length=30, verbose_name="URL в адресній стрічці броузера")

    class Meta:
        verbose_name = "тип товару"
        verbose_name_plural = "типи товарів"

    def __str__(self):
        return "{}/{}".format(self.name_plural, self.section)

    def get_absolute_url(self):
        return reverse(
            'landing:item_type',
            kwargs={
                "department_slug": self.section.department.slug,
                "section_slug": self.section.slug,
                "item_type_slug": self.slug
            }
        )


# Абстрактный класс для единицы товара
@register_eav()
class Item(models.Model):
    # code = models.PositiveIntegerField(default=None, blank=True, verbose_name="код", unique=True, editable=False)
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

    # item_code = models.CharField(default=None,
    #                              blank=True,
    #                              max_length=20)

    gender = models.ForeignKey(properties.Gender, on_delete=models.PROTECT, verbose_name="стать")
    brand = models.ForeignKey(properties.Brand, on_delete=models.PROTECT, verbose_name="виробник")
    fabric = models.ForeignKey(properties.Fabric, on_delete=models.PROTECT, verbose_name="тканина")
    color = models.ForeignKey(properties.Color, on_delete=models.PROTECT, verbose_name="колір")
    size = models.ForeignKey(properties.Size, on_delete=models.PROTECT, verbose_name="розмір")
    slug = models.SlugField(default=None, blank=True, null=True, max_length=30, verbose_name="URL в адресній стрічці броузера")

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товари"

    def __str__(self):
        return "{} - {} ({})".format(self.name, self.item_type, self.price)

    def get_absolute_url(self):
        return reverse(
            'landing:item',
            kwargs={
                "department_slug": self.item_type.section.department.slug,
                "section_slug": self.item_type.section.slug,
                "item_type_slug": self.item_type.slug,
                "item_slug": self.slug
            }
        )


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
