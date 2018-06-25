from django.db import models

# Create your models here.


class Gender(models.Model):
    name = models.CharField(verbose_name="назва", max_length=30)

    class Meta:
        verbose_name = "стать"
        verbose_name_plural = "стать"

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(verbose_name="виробник", max_length=30)
    description = models.CharField(verbose_name="опис", max_length=3000)

    class Meta:
        verbose_name = "виробник"
        verbose_name_plural = "виробники"

    def __str__(self):
        return self.name


class Fabric(models.Model):
    name = models.CharField(verbose_name="назва", max_length=30)
    description = models.CharField(verbose_name="опис", max_length=3000)

    class Meta:
        verbose_name = "тканина"
        verbose_name_plural = "тканини"

    def __str__(self):
        return self.name


class Color(models.Model):
    name = models.CharField(verbose_name="цвет", max_length=30)

    class Meta:
        verbose_name = "колір"
        verbose_name_plural = "кольори"

    def __str__(self):
        return self.name


class Size(models.Model):
    name = models.CharField(verbose_name="размер", max_length=20)

    class Meta:
        verbose_name = "розмір"
        verbose_name_plural = "розміри"

    def __str__(self):
        return self.name

