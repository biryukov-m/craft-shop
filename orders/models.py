from django.db import models
from django.db.models.signals import post_save, post_delete

from product.models import Item
from properties import models as properties

#
# class Status(models.Model):
#     name = models.CharField(null=True,
#                             default=None,
#                             max_length=64,
#                             verbose_name="Програмна назва")
#
#     verbose_name = models.CharField(null=True,
#                                     default=None,
#                                     max_length=64,
#                                     verbose_name="Назва")
#
#     description = models.TextField(blank=True,
#                                    null=True,
#                                    default=None,
#                                    max_length=300,
#                                    verbose_name="Опис")
#
#     def __str__(self):
#         return "{}".format(self.verbose_name)
#
#     class Meta:
#         verbose_name = "Статус замовлення"
#         verbose_name_plural = "Статуси замовлень"


class DeliveryMethod(models.Model):
    name = models.CharField(max_length=50, null=True, verbose_name="Назва")
    description = models.TextField(max_length=300, null=True, verbose_name="Опис")
    created = models.DateTimeField(auto_now=False,
                                   auto_now_add=True,
                                   verbose_name="Створено")
    updated = models.DateTimeField(auto_now=True,
                                   auto_now_add=False,
                                   verbose_name="Оновлено")
    is_available = models.BooleanField(default=True, verbose_name="Доступність")

    class Meta:
        verbose_name = "Спосіб доставки"
        verbose_name_plural = "Способи доставки"

    def __str__(self):
        return '{}'.format(self.name)


class Order(models.Model):
    created = models.DateTimeField(auto_now=False,
                                   auto_now_add=True,
                                   verbose_name="Створено")

    updated = models.DateTimeField(auto_now=True,
                                   auto_now_add=False,
                                   verbose_name="Оновлено")

    code = models.PositiveSmallIntegerField(default=None, blank=True, null=True, editable=False, verbose_name="Код")

    customer_name = models.CharField(max_length=64,
                                     verbose_name="Ім'я покупця")

    customer_email = models.EmailField(max_length=30,
                                       blank=True,
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

    customer_city = models.CharField(max_length=20,
                                     blank=True,
                                     null=True,
                                     default=None,
                                     verbose_name='Місто покупця')

    customer_address = models.CharField(max_length=20,
                                        blank=True,
                                        null=True,
                                        default=None,
                                        verbose_name='Адреса (вулиця, будинок) покупця')

    postal_code = models.PositiveSmallIntegerField(verbose_name='Поштовий код', blank=True, null=True, default=None)

    delivery_method = models.ForeignKey(DeliveryMethod, verbose_name='Спосіб доставки', null=True, on_delete=models.SET_NULL)

    # status = models.ForeignKey(Status,
    #                            on_delete=models.CASCADE,
    #                            default=None,
    #                            blank=True,
    #                            null=True,
    #                            verbose_name="Статус замовлення")

    manager_comment = models.TextField(blank=True,
                                       null=True,
                                       default=None,
                                       max_length=300,
                                       verbose_name="Примітки")

    is_new = models.BooleanField(default=True, editable=False, verbose_name="Нове")
    is_opened = models.BooleanField(default=False, editable=False, verbose_name="Прочитано менеджером")
    is_verified = models.BooleanField(default=False, verbose_name="Інформацію перевірено та підтверджено менеджером")
    is_sent = models.BooleanField(default=False, verbose_name="Відправлено до замовника")
    is_received = models.BooleanField(default=False, verbose_name="Отримано замовником")
    is_paid = models.BooleanField(default=False, verbose_name="Оплачено замовником")

    def __str__(self):
        return "{}. {}, {}.".format(self.code,
                                    self.customer_name.capitalize(),
                                    self.customer_email.lower())

    class Meta:
        verbose_name = "Замовлення"
        verbose_name_plural = "Замовлення"


class Basket(models.Model):
    created = models.DateTimeField(auto_now=False,
                                   auto_now_add=True,
                                   verbose_name="Створено")

    updated = models.DateTimeField(auto_now=True,
                                   auto_now_add=False,
                                   verbose_name="Оновлено")

    session_key = models.CharField(max_length=128,
                                   blank=True,
                                   default=None,
                                   null=True,
                                   verbose_name='Ключ сесії покупця')

    order = models.ForeignKey(Order,
                              on_delete=models.CASCADE,
                              blank=True,
                              null=True,
                              default=None,
                              editable=False,
                              verbose_name='Належність до замовлення')

    total_basket_price = models.DecimalField(blank=True,
                                             null=True,
                                             default=None,
                                             editable=False,
                                             decimal_places=2,
                                             max_digits=10,
                                             verbose_name="Загальна ціна корзини")

    is_closed = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Список корзин'

    def __str__(self):
        if not self.is_closed:
            return 'Корзина анонімна {}'.format(self.session_key)
        else:
            return 'Корзина для замовлення {}'.format(self.order)


class ProductInBasket(models.Model):
    basket = models.ForeignKey(Basket,
                               on_delete=models.CASCADE,
                               blank=True,
                               null=True,
                               default=None,
                               verbose_name="Корзина")

    product = models.ForeignKey(Item,
                                on_delete=models.CASCADE,
                                default=None,
                                verbose_name="Товар")
    quantity = models.PositiveSmallIntegerField(default=1, verbose_name="Одиниць")
    size = models.ForeignKey(properties.Size,
                             on_delete=models.SET_NULL,
                             default=None, blank=True,
                             null=True, verbose_name="Розмір")
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
    created = models.DateTimeField(auto_now=False,
                                   auto_now_add=True,
                                   verbose_name="Створено")
    updated = models.DateTimeField(auto_now=True,
                                   auto_now_add=False,
                                   verbose_name="Оновлено")

    session_key = models.CharField(max_length=128, blank=True, default=None, null=True)

    def __str__(self):
        return '''{} - {}'''.format(self.product.name, self.product.price)

    def save(self, *args, **kwargs):
        try:
            self.one_product_price = self.product.price
            self.total_price = self.quantity*self.one_product_price
            super(ProductInBasket, self).save(*args, **kwargs)
        except:
            print("Вы пытаетесь добавить в заказ товар без или с неправильной ценой/количеством")

    def increase_quantity(self):
        self.quantity += 1
        self.save()
        return self.quantity

    def decrease_quantity(self):
        if self.quantity > 1:
            self.quantity -= 1
            self.save()
            return self.quantity
        else:
            return '''Не можливо зменшити кількість. Кількість = {}'''.format(self.quantity)

    class Meta:
        verbose_name = "Замовлений товар у корзині"
        verbose_name_plural = "Замовлені товари у корзині"

    # class ProductInOrder(models.Model):
    #     order = models.ForeignKey(Order,
    #                               on_delete=models.CASCADE,
    #                               default=None, verbose_name="Замовлення")
    #     product = models.ForeignKey(Item,
    #                                 on_delete=models.CASCADE,
    #                                 default=None,
    #                                 verbose_name="Товар")
    #     quantity = models.PositiveSmallIntegerField(default=1, verbose_name="Одиниць")
    #     one_product_price = models.DecimalField(blank=True,
    #                                             null=True,
    #                                             default=None,
    #                                             editable=False,
    #                                             decimal_places=2,
    #                                             max_digits=10,
    #                                             verbose_name="Ціна за одну одиницю")
    #     total_price = models.DecimalField(blank=True,
    #                                       null=True,
    #                                       default=None,
    #                                       editable=False,
    #                                       decimal_places=2,
    #                                       max_digits=10,
    #                                       verbose_name="Загальна ціна по товару")
    #     is_inactive = models.BooleanField(default=False, verbose_name="Товар відмінено")
    #     created = models.DateTimeField(auto_now=False,
    #                                    auto_now_add=True,
    #                                    verbose_name="Створено")
    #     updated = models.DateTimeField(auto_now=True,
    #                                    auto_now_add=False,
    #                                    verbose_name="Оновлено")
    #
    #     def __str__(self):
    #         return '''{} - {}'''.format(self.product.name, self.product.price)
    #
    #     def save(self, *args, **kwargs):
    #         try:
    #             self.one_product_price = self.product.price
    #             self.total_price = self.quantity*self.one_product_price
    #         except:
    #             print("Вы пытаетесь добавить в заказ товар без или с неправильной ценой/количеством")
    #             raise ValueError
    #         super(ProductInOrder, self).save(*args, **kwargs)
    #
    #     class Meta:
    #         verbose_name = "Замовлений товар"
    #         verbose_name_plural = "Замовлені товари"
    #


# def count_order_total_price(instance, **kwargs):
#     all_products_in_order = ProductInOrder.objects.filter(order=instance.order, is_inactive=False)
#     order_total_price = 0
#     for product in all_products_in_order:
#         order_total_price += product.total_price
#     instance.order.total_price = order_total_price
#     instance.order.save(force_update=True)
# post_save.connect(count_order_total_price, sender=ProductInOrder)
# post_delete.connect(count_order_total_price, sender=ProductInOrder)

def post_save_for_order(instance, **kwargs):
    if not instance.code:
        code = instance.pk + 100
        instance.code = code
        instance.save()


post_save.connect(post_save_for_order, sender=Order)
