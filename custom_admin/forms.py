from django import forms

from orders.models import Order
from orders.models import DeliveryMethod
from orders.models import Status
from properties.models import Fabric
from properties.models import Color
from properties.models import Brand
from properties.models import Size
from product.models import ItemType
from product.models import Item
from product.models import ItemImage

import django_filters


class OrderFilter(django_filters.FilterSet):
    code = django_filters.CharFilter(lookup_expr='iexact')
    customer_name = django_filters.CharFilter(lookup_expr='iexact')
    customer_email = django_filters.CharFilter(lookup_expr='iexact')
    customer_phone = django_filters.CharFilter(lookup_expr='icontains')
    delivery_method = django_filters.ModelMultipleChoiceFilter(queryset=DeliveryMethod.objects.all(), widget=forms.CheckboxSelectMultiple)
    status = django_filters.ModelMultipleChoiceFilter(queryset=Status.objects.all(), widget=forms.CheckboxSelectMultiple)
    is_removed = django_filters.BooleanFilter()


class ItemFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    price = django_filters.RangeFilter(field_name='price')
    available_sizes = django_filters.ModelMultipleChoiceFilter(queryset=Size.objects.all(), widget=forms.CheckboxSelectMultiple)
    fabric = django_filters.ModelMultipleChoiceFilter(queryset=Fabric.objects.all(), widget=forms.CheckboxSelectMultiple)
    color = django_filters.ModelMultipleChoiceFilter(queryset=Color.objects.all(), widget=forms.CheckboxSelectMultiple)
    brand = django_filters.ModelMultipleChoiceFilter(queryset=Brand.objects.all(), widget=forms.CheckboxSelectMultiple)
    item_type = django_filters.ModelMultipleChoiceFilter(queryset=ItemType.objects.all(), widget=forms.CheckboxSelectMultiple)


class OrderAdminForm(forms.ModelForm):
    class Meta:
        model = Order
        # exclude = ('hash_code', 'session_key')
        fields = (
            'customer_name',
            'customer_email',
            'customer_phone',
            'customer_comment',
            'customer_city',
            'customer_address',
            'postal_code',
            'delivery_method',
            'status',
            'manager_comment',
            'is_removed',
            'hash_code',
        )

        widgets = {
            'status': forms.CheckboxSelectMultiple(choices=Status.objects.all()),
        }

    def __init__(self, *args, **kwargs):
        super(OrderAdminForm, self).__init__(*args, **kwargs)
        self.fields['delivery_method'].empty_label = "Оберіть спосіб доставки..."


class ProductAdminForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name',
                  'item_type',
                  'description',
                  'price',
                  'available',
                  'brand',
                  'fabric',
                  'color',
                  'available_sizes',
                  'slug',)


class ImageAdminForm(forms.ModelForm):
    class Meta:
        model = ItemImage
        fields = ('image',
                  'item_related',
                  'is_basic',
                  'is_active',)


class ProductImageForm(forms.ModelForm):
    class Meta:
        model = ItemImage
        exclude = ('is_basic',)
