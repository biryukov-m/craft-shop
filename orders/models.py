from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_save, post_delete


class Status(models.Model):
    name = models.CharField(null=True,
                            default=None,
                            max_length=64,
                            verbose_name="Назва статуса")

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        verbose_name = "Статус замовлення"
        verbose_name_plural = "Статуси замовлень"


class Order(models.Model):
    created = models.DateTimeField(auto_now=False,
                                   auto_now_add=True,
                                   verbose_name="Створено")

    updated = models.DateTimeField(auto_now=True,
                                   auto_now_add=False,
                                   verbose_name="Оновлено")

    customer_name = models.CharField(max_length=64,
                                     verbose_name="Ім'я покупця")

    customer_email = models.EmailField(blank=True,
                                       null=True,
                                       default=None,
                                       verbose_name="Електронна пошта покупця")

    customer_phone = models.CharField(blank=True,
                                      null=True,
                                      default=None,
                                      max_length=40,
                                      verbose_name="Телефон покупця")

    customer_comment = models.TextField(blank=True,
                                        null=True,
                                        default=None,
                                        max_length=300,
                                        verbose_name="Комментар до замовлення")

    status = models.ForeignKey(Status,
                               on_delete=models.CASCADE,
                               default=None,
                               verbose_name="Статус замовлення")

    total_price = models.DecimalField(blank=True,
                                      null=True,
                                      default=None,
                                      editable=False,
                                      decimal_places=2,
                                      max_digits=10,
                                      verbose_name="Загальна ціна замовлення")

    def __str__(self):
        return "{}. {}, {}. {}. {}".format(self.id,
                                           self.customer_name.capitalize(),
                                           self.customer_email.lower(),
                                           self.total_price,
                                           self.status.name)

    class Meta:
        verbose_name = "Замовлення"
        verbose_name_plural = "Замовлення"


class ProductInOrder(models.Model):
    order = models.ForeignKey(Order,
                              on_delete=models.CASCADE,
                              default=None, verbose_name="Замовлення")

    # Реализация Generic Foreign Key так как моделей товаров много
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, verbose_name="Тип товару")
    object_id = models.PositiveIntegerField(verbose_name="ID товару")
    product_object = GenericForeignKey('content_type', 'object_id')

    quantity = models.PositiveSmallIntegerField(default=1, verbose_name="Одиниць")

    one_product_price = models.DecimalField(blank=True,
                                            null=True,
                                            default=None,
                                            editable=False,
                                            decimal_places=2,
                                            max_digits=10,
                                            verbose_name="Ціна за одну одиницю")

    total_price = models.DecimalField(blank=True,
                                      null=True,
                                      default=None,
                                      editable=False,
                                      decimal_places=2,
                                      max_digits=10,
                                      verbose_name="Загальна ціна по товару")

    is_inactive = models.BooleanField(default=False, verbose_name="Товар відмінено")

    created = models.DateTimeField(auto_now=False,
                                   auto_now_add=True,
                                   verbose_name="Створено")

    updated = models.DateTimeField(auto_now=True,
                                   auto_now_add=False,
                                   verbose_name="Оновлено")

    def __str__(self):
        return '''{}/{} - {}'''.format(self.content_type.name.capitalize(),
                                       self.product_object.name.capitalize(),
                                       self.product_object.price)

    def save(self, *args, **kwargs):
        try:
            self.one_product_price = self.product_object.price
            self.total_price = self.quantity*self.one_product_price
        except:
            print("Вы пытаетесь добавить в заказ товар без или с неправильной ценой/количеством")
            raise ValueError
        super(ProductInOrder, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Замовлений товар"
        verbose_name_plural = "Замовлені товари"


def count_order_total_price(instance, **kwargs):
    all_products_in_order = ProductInOrder.objects.filter(order=instance.order, is_inactive=False)
    order_total_price = 0
    for product in all_products_in_order:
        order_total_price += product.total_price
    instance.order.total_price = order_total_price
    instance.order.save(force_update=True)

post_save.connect(count_order_total_price, sender=ProductInOrder)
post_delete.connect(count_order_total_price, sender=ProductInOrder)