from django.shortcuts import render
from django.shortcuts import get_object_or_404
from orders.models import Order
from django.views import View

from .forms import OrderFilter
from .forms import OrderAdminForm


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


class OrdersList(View):
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


class OrderDetail(View):
    template_name = 'custom_admin/order_detail.html'

    def get(self, request, order_code, *args, **kwargs):
        order = get_object_or_404(Order, code=order_code)
        order_admin_form = OrderAdminForm(instance=order)
        context = {'order': order, 'order_admin_form': order_admin_form}
        return render(request, template_name=self.template_name, context=context)
