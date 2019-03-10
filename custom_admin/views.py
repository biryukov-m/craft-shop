from django.shortcuts import render
from orders.models import Order


def main(request):
    template = 'custom_admin/main.html'
    return render(request, template)


def orders(request):
    template = 'custom_admin/orders.html'
    orders_query = Order.objects.all()
    context = dict()
    context['orders_query'] = orders_query
    return render(request, template, context)
