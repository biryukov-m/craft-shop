from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import reverse

from django.views import View
from orders.models import Order
from product.models import Department
from product.models import Item
from django.db.models import Max, Min

from .forms import OrderFilter
from .forms import ItemFilter
from .forms import OrderAdminForm


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
        form = OrderAdminForm(instance=order)
        context = {'order': order, 'order_admin_form': form}
        return render(request, template_name=self.template_name, context=context)

    def post(self, request, order_code, *args, **kwargs):
        order = get_object_or_404(Order, code=order_code)
        form = OrderAdminForm(request.POST, instance=order)
        if form.is_valid():
            order = form.save(commit=False)
            order.save()
            print("Форму збережено - {}".format(order))
            print(order.status)
        else:
            print("Помилка в редагуванні форми замовлення у адмін-інтерфейса")
            context = {'order': order, 'order_admin_form': form}
            for f in form.fields:
                if form.has_error(f):
                    print("Помилка у полі: ", form.has_error(f))
            return render(request, template_name=self.template_name, context=context)
        return redirect(order.get_absolute_admin_url())


class OrderRemove(View):

    def get(self, request, order_code, *args, **kwargs):
        order = get_object_or_404(Order, code=order_code)
        print("Видаляю замовлення: ", order)
        order.is_removed = True
        order.save()
        return redirect(reverse('custom_admin:orders'))


# Поведение с товарами
class AllProducts(View):
    template_name = 'custom_admin/products.html'

    def get_context_data(self, request, *args, **kwargs):
        sidebar = {}
        departments = Department.objects.all()
        for department in departments:
            sidebar[department] = {}
            for section in department.get_sections():
                sidebar[department][section] = []
                for item_type in section.get_item_types():
                    sidebar[department][section].append(item_type)
        items_list = Item.objects.all()
        item_filter = ItemFilter(request.GET, queryset=items_list)
        form = item_filter.form
        context = locals()
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(request, *args, **kwargs)
        return render(request, self.template_name, context=context)