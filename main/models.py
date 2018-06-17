from django.db import models

# Create your models here.


class Item(models.Model):
    code = models.IntegerField(default=None, blank=True, verbose_name="Код")
    name = models.CharField(default=None, blank=True, verbose_name='Наименование')
    description = models.TextField(default=None, verbose_name='Описание')
    photo = models.ImageField(default=None, blank=True, verbose_name='Основное фото')
    price = models.IntegerField(default=None, blank=True, verbose_name='Цена')
    available = models.BooleanField(default=False, verbose_name='Размещен в продажу')

    class Meta:
        abstract = True


class Genders(models.Model):
    name = models.CharField(verbose_name="Назначение")


class Brand(models.Model):
    name = models.CharField(verbose_name="Производитель")
    description = models.CharField(verbose_name="Описание")


class Fabric(models.Model):
    name = models.CharField(verbose_name="Ткань")


class Color(models.Model):
    name = models.CharField(verbose_name="Цвет")


class Size(models.Model):
    name = models.CharField(verbose_name="Размер")


class Clothes(Item):
    gender = models.ForeignKey(Genders, on_delete=models.PROTECT)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT)
    fabric = models.ForeignKey(Fabric, on_delete=models.PROTECT)
    color = models.ForeignKey(Color, on_delete=models.PROTECT)
    size = models.ForeignKey(Size, on_delete=models.PROTECT)

    class Meta:
        abstract = True

