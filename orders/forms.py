from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('customer_name', 'customer_email', 'customer_phone', 'delivery_method',  'postal_code', 'customer_city', 'customer_address',  'customer_comment')

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['delivery_method'].empty_label = "Оберіть спосіб доставки..."
        # self.fields['delivery_method'].queryset = Choice.objects.all().values_list('id', 'field')