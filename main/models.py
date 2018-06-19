from django.db import models


# Абстрактный класс для единицы товара

class Item(models.Model):
    code = models.PositiveIntegerField(default=None, blank=True, verbose_name="код", unique=True, editable=False)
    name = models.CharField(default=None, blank=True, verbose_name='наименование', max_length=40)
    description = models.TextField(default=None, verbose_name='описание', max_length=3000)
    photo = models.ImageField(default=None, blank=True, verbose_name='основное фото')
    price = models.IntegerField(default=None, blank=True, verbose_name='цена')
    available = models.BooleanField(default=False, verbose_name='доступен')

    class Meta:
        abstract = True


class Genders(models.Model):
    name = models.CharField(verbose_name="название", max_length=30)

    class Meta:
        verbose_name = "стать"
        verbose_name_plural = "стать"


class Brand(models.Model):
    name = models.CharField(verbose_name="производитель", max_length=30)
    description = models.CharField(verbose_name="описание", max_length=3000)

    class Meta:
        verbose_name = "виробник"
        verbose_name_plural = "виробники"


class Fabric(models.Model):
    name = models.CharField(verbose_name="название", max_length=30)
    description = models.CharField(verbose_name="описание", max_length=3000)

    class Meta:
        verbose_name = "тканина"
        verbose_name_plural = "тканини"


class Color(models.Model):
    name = models.CharField(verbose_name="цвет", max_length=30)

    class Meta:
        verbose_name = "колір"
        verbose_name_plural = "кольори"


class Size(models.Model):
    name = models.CharField(verbose_name="размер", max_length=20)

    class Meta:
        verbose_name = "розмір"
        verbose_name_plural = "розміри"


# Абстрактный класс для элементов одежды

class Clothes(Item):
    gender = models.ForeignKey(Genders, on_delete=models.PROTECT, verbose_name="стать")
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, verbose_name="виробник")
    fabric = models.ForeignKey(Fabric, on_delete=models.PROTECT, verbose_name="тканина")
    color = models.ForeignKey(Color, on_delete=models.PROTECT, verbose_name="колір")
    size = models.ForeignKey(Size, on_delete=models.PROTECT, verbose_name="розмір")

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


# Товары

class Shirt(Clothes):

    class Meta:
        verbose_name = "сорочка"
        verbose_name_plural = "сорочки"


class ShirtPattern(Clothes, Pattern):

    class Meta:
        verbose_name = "заготовка сорочки"
        verbose_name_plural = "заготовки сорочок"


class TShirt(Clothes):

    class Meta:
        verbose_name = "футболка"
        verbose_name_plural = "футболки"


class TShirtPattern(Clothes, Pattern):

    class Meta:
        verbose_name = "заготовка футболки"
        verbose_name_plural = "заготовки футболок"


class Dress(Clothes):

    class Meta:
        verbose_name = "сукня"
        verbose_name_plural = "сукні"


class DressPattern(Clothes, Pattern):

    class Meta:
        verbose_name = "заготовка сукні"
        verbose_name_plural = "заготовки суконь"


class Tunic(Clothes):

    class Meta:
        verbose_name = "туніка"
        verbose_name_plural = "туніки"


class TunicPattern(Clothes, Pattern):

    class Meta:
        verbose_name = "заготовка туніки"
        verbose_name_plural = "заготовки тунік"


class Skirt(Clothes):

    class Meta:
        verbose_name = "спідниця"
        verbose_name_plural = "спідниці"


class SkirtPattern(Clothes, Pattern):

    class Meta:
        verbose_name = "заготовка спідниці"
        verbose_name_plural = "заготовки спідниць"


# Аксессуари


class Bag(Item):

    class Meta:
        verbose_name = "сумка"
        verbose_name_plural = "сумки"


class CosmeticBag(Item):

    class Meta:
        verbose_name = "косметичка"
        verbose_name_plural = "косметички"


class MobileCase(Item):

    class Meta:
        verbose_name = "чохол для мобільного телефону"
        verbose_name_plural = "чохли для мобільних телефонів"


class TableCloth(Item):

    class Meta:
        verbose_name = "скатертина"
        verbose_name_plural = "скатертини"