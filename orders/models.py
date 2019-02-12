from django.db import models
from django.db.models.signals import post_save
from django.shortcuts import reverse
from product.models import Item
from properties import models as properties
from utils.generators import generate_order_hash


class Status(models.Model):
    name = models.CharField(null=True,
                            default=None,
                            max_length=64,
                            verbose_name="Програмна назва")

    verbose_name = models.CharField(null=True,
                                    default=None,
                                    max_length=64,
                                    verbose_name="Назва")

    description = models.TextField(blank=True,
                                   null=True,
                                   default=None,
                                   max_length=300,
                                   verbose_name="Опис")

    number = models.PositiveSmallIntegerField(null=True, blank=True, default=True, verbose_name='Порядковий номер')

    def __str__(self):
        return "{} - {}".format(self.number, self.verbose_name)

    class Meta:
        verbose_name = "Статус замовлення"
        verbose_name_plural = "Статуси замовлень"


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

    hash_code = models.CharField(default=None, blank=True, null=True, editable=False, max_length=64, verbose_name='хеш-код')

    session_key = models.CharField(max_length=128,
                                   null=True,
                                   verbose_name='Ключ сесії покупця')

    customer_name = models.CharField(max_length=64,
                                     verbose_name="Ім'я покупця")

    customer_email = models.EmailField(max_length=30,
                                       null=True,
                                       verbose_name="Електронна пошта покупця")

    customer_phone = models.CharField(null=True,
                                      max_length=40,
                                      verbose_name="Телефон покупця")

    customer_comment = models.TextField(blank=True,
                                        null=True,
                                        default=None,
                                        max_length=300,
                                        verbose_name="Комментар до замовлення")

    customer_city = models.CharField(max_length=20,
                                     null=True,
                                     verbose_name='Місто покупця')

    customer_address = models.CharField(max_length=20,
                                        null=True,
                                        verbose_name='Адреса (вулиця, будинок) покупця')

    postal_code = models.PositiveSmallIntegerField(verbose_name='Поштовий код', blank=True, null=True, default=None)

    delivery_method = models.ForeignKey(DeliveryMethod, verbose_name='Спосіб доставки', null=True, on_delete=models.SET_NULL)

    status = models.ManyToManyField(Status,
                                    default=None,
                                    blank=True,
                                    null=True,
                                    verbose_name="Статус замовлення")

    manager_comment = models.TextField(blank=True,
                                       null=True,
                                       default=None,
                                       max_length=300,
                                       verbose_name="Примітки")

    def __str__(self):
        return "№ {}. {}, {}.".format(self.code,
                                      self.customer_name.capitalize(),
                                      self.customer_email.lower())

    def get_items(self):
        return self.basket.productinbasket_set.all()

    def get_absolute_url(self):
        url = reverse('orders:single_order_hash_code', kwargs={"hash_code": self.hash_code})
        return url

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

    order = models.OneToOneField(Order,
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

    def save(self, *args, **kwargs):
        if self.productinbasket_set.all():
            sum_ = 0
            for prod in self.productinbasket_set.all():
                sum_ += prod.total_price
            self.total_basket_price = sum_
        super(Basket, self).save(*args, **kwargs)


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


def post_save_for_order(instance, **kwargs):
    if not (instance.code or instance.hash_code):
        code = instance.pk + 100
        hash_code = generate_order_hash(code)
        instance.code = code
        instance.hash_code = hash_code
        instance.save()


post_save.connect(post_save_for_order, sender=Order)
