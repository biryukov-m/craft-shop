from django.db import models

from urllib.parse import urlencode
# Create your models here.


class Gender(models.Model):
    name = models.CharField(verbose_name="назва", max_length=30)
    slug = models.SlugField(default=None, blank=True, null=True, max_length=30, verbose_name="URL в адресній стрічці броузера")

    class Meta:
        verbose_name = "стать"
        verbose_name_plural = "стать"

    def __str__(self):
        return self.name

    def get_search_param(self):
        params = '?gender={}'.format(self.slug)
        return params


class Brand(models.Model):
    name = models.CharField(verbose_name="виробник", max_length=30)
    description = models.TextField(verbose_name="опис", max_length=30000)
    slug = models.SlugField(default=None, blank=True, null=True, max_length=30, verbose_name="URL в адресній стрічці броузера")

    class Meta:
        verbose_name = "виробник"
        verbose_name_plural = "виробники"

    def __str__(self):
        return self.name

    def get_search_param(self):
        params = '?brand={}'.format(self.slug)
        return params


class Fabric(models.Model):
    name = models.CharField(verbose_name="назва", max_length=30)
    description = models.TextField(verbose_name="опис", max_length=30000)
    slug = models.SlugField(default=None, blank=True, null=True, max_length=30, verbose_name="URL в адресній стрічці броузера")

    class Meta:
        verbose_name = "тканина"
        verbose_name_plural = "тканини"

    def __str__(self):
        return self.name

    def get_search_param(self):
        params = '?fabric={}'.format(self.slug)
        return params


class Color(models.Model):
    name = models.CharField(verbose_name="колір", max_length=30)
    slug = models.SlugField(default=None, blank=True, null=True, max_length=30, verbose_name="URL в адресній стрічці броузера")

    class Meta:
        verbose_name = "колір"
        verbose_name_plural = "кольори"

    def __str__(self):
        return self.name

    def get_search_param(self):
        params = '?color={}'.format(self.slug)
        return params


class Size(models.Model):
    name = models.CharField(verbose_name="розмір", max_length=20)
    slug = models.SlugField(default=None, blank=True, null=True, max_length=30, verbose_name="URL в адресній стрічці броузера")

    class Meta:
        verbose_name = "розмір"
        verbose_name_plural = "розміри"

    def __str__(self):
        return self.name



