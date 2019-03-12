from django.shortcuts import render
from orders.models import Order
from django.views import View

from .forms import OrderFilter


def main(request):
    template = 'custom_admin/main.html'
    return render(request, template)


class Main(View):
    template_name = 'custom_admin/main.html'

    def get_context_data(self, request, *args, **kwargs):
        orders_list = Order.objects.all()
        order_filter = OrderFilter(request.GET, queryset=orders_list)
        form = order_filter.form
        context = locals()
        context['breadcrumbs'] = "Усі замовлення"

        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(request, *args, **kwargs)
        return render(request, self.template_name, context=context)


class Orders(View):
    template_name = 'custom_admin/orders.html'

    def get_context_data(self, request, *args, **kwargs):
        orders_list = Order.objects.all()
        order_filter = OrderFilter(request.GET, queryset=orders_list)
        form = order_filter.form
        context = locals()
        context['breadcrumbs'] = "Усі замовлення"

        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(request, *args, **kwargs)
        return render(request, self.template_name, context=context)
