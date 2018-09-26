import django_filters
from product.models import Item


class ProductFilter(django_filters.FilterSet):
    # name = django_filters.CharFilter(lookup_expr='iexact')
    #
    # price = django_filters.NumberFilter()
    # price__gt = django_filters.NumberFilter(field_name='price', lookup_expr='gt')
    # price__lt = django_filters.NumberFilter(field_name='price', lookup_expr='lt')
    #
    # # brand__name = django_filters.MultipleChoiceFilter(field_name='brand__name', lookup_expr='iexact')
    # # gender__name = django_filters.MultipleChoiceFilter(field_name='gender__name', lookup_expr='iexact')
    # # fabric__name = django_filters.MultipleChoiceFilter(field_name='fabric__name', lookup_expr='iexact')
    # # color__name = django_filters.MultipleChoiceFilter(field_name='color__name', lookup_expr='iexact')
    # brand__name = django_filters.ChoiceFilter(field_name='brand__name', lookup_expr='iexact')
    # gender = django_filters.ChoiceFilter(field_name='gender__name', lookup_expr='iexact')
    # fabric = django_filters.ChoiceFilter(field_name='fabric__name', lookup_expr='iexact')
    # color = django_filters.ChoiceFilter(field_name='color__name', lookup_expr='iexact')

    class Meta:
        model = Item
        fields = ['price', 'brand', 'gender', 'fabric', 'color', 'size', 'item_type']