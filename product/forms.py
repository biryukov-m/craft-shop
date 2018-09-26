import django_filters
from product.models import Item


class ProductFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='iexact')

    price = django_filters.NumberFilter()
    price__gt = django_filters.NumberFilter(field_name='price', lookup_expr='gt')
    price__lt = django_filters.NumberFilter(field_name='price', lookup_expr='lt')

    brand__name = django_filters.MultipleChoiceFilter(field_name='brand__name')
    gender__name = django_filters.MultipleChoiceFilter(field_name='gender__name')
    fabric__name = django_filters.MultipleChoiceFilter(field_name='fabric__name')
    color__name = django_filters.MultipleChoiceFilter(field_name='color__name')

    # class Meta:
        # model = Item