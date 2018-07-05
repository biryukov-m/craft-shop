from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class Status(models.Model):
    name = models.CharField(blank=True, null=True, default=None, max_length=64, verbose_name="Назва статуса")

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        verbose_name = "Статус замовлення"
        verbose_name_plural = "Статуси замовлень"


class Order(models.Model):
    created = models.DateTimeField(auto_now=False, auto_now_add=True, verbose_name="Создан")
    updated = models.DateTimeField(auto_now=True, auto_now_add=False, verbose_name="Обновлен")
    customer_name = models.CharField(max_length=64, verbose_name="Имя покупця")
    customer_email = models.EmailField(blank=True, null=True, default=None, verbose_name="Електронна пошта покупця")
    customer_phone = models.CharField(blank=True, null=True, default=None, max_length=40, verbose_name="Телефон покупця")
    customer_comment = models.TextField(blank=True, null=True, default=None, max_length=300, verbose_name="Комментар до замовлення")
    status = models.ForeignKey(Status, on_delete=models.CASCADE, default=None, verbose_name="Статус замовлення")
    total_price = models.DecimalField(default=None, decimal_places=2, max_digits=10, verbose_name="Загальна ціна замовлення")

    def __str__(self):
        return "Замовлення {} - {}".format(self.id, self.status.name)

    class Meta:
        verbose_name = "Замовлення"
        verbose_name_plural = "Замовлення"


class ProductInOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, default=None)

    # Реализация Generic Foreign Key так как моделей товаров много
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    product_object = GenericForeignKey('content_type', 'object_id')

    quantity = models.PositiveSmallIntegerField(default=1)
    one_product_price = models.DecimalField(default=None, decimal_places=2, max_digits=10, verbose_name="ціна за одну одиницю")
    total_price = models.DecimalField(default=None, decimal_places=2, max_digits=10, verbose_name="загальна ціна по товару")
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return "Замовлений товар {}".format(self.id)

    def save(self, *args, **kwargs):
        try:
            self.one_product_price = self.product_object.price
        except:
            print("Вы пытаетесь добавить в заказ товар без или с неправильной ценой")
        self.total_price = self.quantity*self.one_product_price
        super(ProductInOrder, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Замовлений товар"
        verbose_name_plural = "Замовлені товари"
