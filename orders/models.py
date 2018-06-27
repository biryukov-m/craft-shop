from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class Order(models.Model):
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    customer_name = models.CharField(max_length=64)
    customer_email = models.EmailField(blank=True, null=True, default=None)
    customer_phone = models.CharField(blank=True, null=True, default=None, max_length=40)
    customer_comment = models.CharField(blank=True, null=True, default=None, max_length=300)

    def __str__(self):
        return "Заказ {}".format(self.id)

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"


class ProductInOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True, default=None)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    product_object = GenericForeignKey('content_type', 'object_id')

    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    customer_name = models.CharField(max_length=64)
    customer_email = models.EmailField(default=None, blank=True, null=True)
    customer_phone = models.CharField(default=None, blank=True, null=True, max_length=40)
    customer_comment = models.CharField(default=None, blank=True, null=True, max_length=300)

    def __str__(self):
        return "Заказ {}".format(self.id)

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
