from django import forms

from properties.models import Fabric
from properties.models import Color
from properties.models import Brand
from properties.models import Size

import django_filters


class ProductFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='iexact')
    price = django_filters.RangeFilter(field_name='price')
    available_sizes = django_filters.ModelMultipleChoiceFilter(queryset=Size.objects.all(), widget=forms.CheckboxSelectMultiple)
    # available_sizes = django_filters.ModelMultipleChoiceFilter()
    fabric = django_filters.ModelMultipleChoiceFilter(queryset=Fabric.objects.all(), widget=forms.CheckboxSelectMultiple)
    color = django_filters.ModelMultipleChoiceFilter(queryset=Color.objects.all(), widget=forms.CheckboxSelectMultiple)
    brand = django_filters.ModelMultipleChoiceFilter(queryset=Brand.objects.all(), widget=forms.CheckboxSelectMultiple)