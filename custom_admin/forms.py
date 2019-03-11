from django import forms
from orders.models import Order
from orders.models import DeliveryMethod
from orders.models import Status


import django_filters


class OrderFilter(django_filters.FilterSet):
    code = django_filters.CharFilter(lookup_expr='iexact')
    customer_name = django_filters.CharFilter(lookup_expr='iexact')
    customer_email = django_filters.CharFilter(lookup_expr='iexact')
    customer_phone = django_filters.CharFilter(lookup_expr='icontains')
    delivery_method = django_filters.ModelMultipleChoiceFilter(queryset=DeliveryMethod.objects.all(), widget=forms.CheckboxSelectMultiple)
    status = django_filters.ModelMultipleChoiceFilter(queryset=Status.objects.all(), widget=forms.CheckboxSelectMultiple)
