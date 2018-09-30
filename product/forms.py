from django import forms

from product.models import Item
from properties.models import Fabric
from properties.models import Color
from properties.models import Brand
from properties.models import Gender
from properties.models import Size

import django_filters


class ProductFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='iexact')

    price = django_filters.RangeFilter(field_name='price')

    size = django_filters.ModelMultipleChoiceFilter(queryset=Size.objects.all())
    fabric = django_filters.ModelMultipleChoiceFilter(field_name='fabric', lookup_expr='exact', queryset=Fabric.objects.all())
    color = django_filters.ModelMultipleChoiceFilter(field_name='color', lookup_expr='exact', queryset=Color.objects.all())
    brand = django_filters.ModelMultipleChoiceFilter(
        field_name='brand',
        lookup_expr='exact',
        queryset=Brand.objects.all(),
        widget=forms.CheckboxSelectMultiple
        )
    gender = django_filters.ModelMultipleChoiceFilter(field_name='gender', lookup_expr='exact', queryset=Gender.objects.all())
    #
    # class Meta:
    #     model = Item
    #     fields = {
    #         'price': ['lte', 'gte'],
    #         'size': ['lte', 'gte'],
    #         'fabric': ['exact'],
    #         'color': ['exact'],
    #         'brand': ['exact'],
    #     }