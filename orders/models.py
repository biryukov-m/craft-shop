from django.db import models
from product.models import

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
    product = models.ForeignKey()

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
