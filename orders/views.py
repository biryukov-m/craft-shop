from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.http import HttpResponse
from django.http import Http404
from django.views.generic import View
from .models import ProductInBasket
from .models import Basket
from .models import Order
from .models import Status
from product.models import Item
from properties.models import Size
from .forms import OrderForm
from .utils import render_to_pdf


def basket_add(request):
    return_dict = dict()
    session_key = request.session.session_key
    print('Executing basket add. Session key is {}'.format(session_key))
    data = request.POST
    print('POST is {}'.format(data))
    item_id = data.get('item_id')
    item_quantity = int(data.get('item_quantity'))
    item_size = data.get('item_size')
    print('Ajax item size - ', item_size)
    item_size = Size.objects.get(name=item_size)
    print('Found in BD item size - ', item_size)
    item = Item.objects.get(id=item_id)
    print('Item is {}'.format(item))
    print('Searching for session key associate basket...')
    basket, basket_created = Basket.objects.get_or_create(session_key=session_key, is_closed=False)
    print('Variable basket_created is {}'.format(basket_created))
    print('Basket is {}'.format(basket))
    print('Searching for instance of item in basket...')
    new_product, created = ProductInBasket.objects.get_or_create(session_key=session_key,
                                                                 product=item,
                                                                 size=item_size,
                                                                 basket=basket,
                                                                 defaults={"quantity": item_quantity})
    if not created:
        new_product.quantity += item_quantity
        new_product.save(force_update=True)
        print('Found  {}'.format(new_product))
    else:
        print('Not found instance, created product is {}'.format(new_product))
    items_total_number = ProductInBasket.objects.filter(basket=basket).count()
    return_dict["items_total_number"] = items_total_number
    print('Total number of items in basket is {}'.format(items_total_number))
    return JsonResponse(return_dict)


def basket_change_quantity(request):
    return_dict = dict()
    session_key = request.session.session_key
    data = request.POST
    item_id = data.get('item_id')
    print('Got from AJAX item_id - ', item_id)
    item_quantity = int(data.get('item_quantity'))
    print('Got from AJAX item_quantity - ', item_quantity)
    item_size = data.get('item_size')
    print('Got from AJAX item_size - ', item_size)
    item_size = Size.objects.get(name=item_size)
    print('Found in BD item_size - ', item_size)
    item = Item.objects.get(id=item_id)
    print('Found in BD item', item)
    method = data.get('method')
    print('Got from AJAX method - ', method)
    print('Trying to find product')
    try:
        product = ProductInBasket.objects.get(
            session_key=session_key,
            product=item,
            size=item_size,
            quantity=item_quantity,
            basket__is_closed=False)
        print('Found product', product)
    except:
        print('''
        Can't find product with this query: 
        ProductInBasket.objects.get(session_key={}, product={}, size={}, quantity={})
        '''.format(session_key, item, item_size, item_quantity))
        product = None
    if product:
        print('''
        Found product with this query: 
        ProductInBasket.objects.get(session_key={}, product={}, size={}, quantity={})
        '''.format(session_key, item, item_size, item_quantity))
        if method == 'increase':
            print('Increasing quantity...')
            product.quantity += 1
            product.save()
            print('New quantity =', product.quantity)
        elif method == 'decrease':
            if product.quantity > 1:
                print('Decreasing quantity...')
                product.quantity -= 1
                product.save()
                print('New quantity =', product.quantity)
            else:
                return_dict["response"] = '''Wrong item quantity, can't decrease, because quantity <= 1'''
        else:
            return_dict["response"] = '''Wrong method. Must be "decrease" or "increase"'''

    items_total_number = ProductInBasket.objects.filter(session_key=session_key, basket__is_closed=False).count()
    return_dict["items_total_number"] = items_total_number
    return JsonResponse(return_dict)


def basket_remove(request):
    return_dict = dict()
    session_key = request.session.session_key
    data = request.POST
    item_id = data.get('item_id')
    item_size = data.get('item_size')
    try:
        item_size = Size.objects.get(name=item_size)
        print('Found in BD item size - ', item_size)
    except:
        print('Received Ajax item size ', item_size)
        print("Error. Can't find item size in BD ", item_size)
        return
    try:
        basket = Basket.objects.get(session_key=session_key, is_closed=False)
    except:
        print("Internal error. Didn't find basket with session key {}".format(session_key))
        return
    try:
        item = ProductInBasket.objects.get(basket=basket, id=item_id, size=item_size)
        print('Deleting item {} ...'.format(item))
        item.delete()
        print('Item deleted')
    except:
        print("Can't find item with that query: ProductInBasket.objects.get(basket={}, id={}, size={})".format(basket, item_id, item_size))
        return
    if not basket.productinbasket_set.all():
        print('No items in basket left. Deleting basket...')
        basket.delete()
        print('Basket deleted')
    else:
        items_total_number = basket.productinbasket_set.all().count()
        print('Total number of items: {}'.format(items_total_number))
        return_dict["items_total_number"] = items_total_number
    return JsonResponse(return_dict)


def checkout(request):
    print('Executing checkout view...')
    template_name = 'orders/checkout.html'
    context = {}
    session_key = request.session.session_key
    form = OrderForm(request.POST)
    context['form'] = form
    if not Basket.objects.filter(session_key=session_key, is_closed=False).exists():
        print('User has no opened basket, so he cant use checkout, returning 404')
        raise Http404
    if request.method == 'POST':
        print("Request method is POST, checking if form is valid...")
        if form.is_valid:
            print("Form is valid.")
            print("Got POST with parameters {}".format(request.POST))
            session_key = request.session.session_key
            try:
                basket = Basket.objects.get(session_key=session_key, is_closed=False)
            except:
                print("Can't get basket from checkout with parameters: "
                      "Basket.objects.get(session_key={}, is_closed=False)".format(session_key))
                return render(request, template_name, context=context)
            if basket:
                new_order = form.save(commit=False)
                new_order.session_key = session_key
                new_order.save()
                basket.order = new_order
                basket.is_closed = True
                basket.save()

        return redirect('orders:checkout_success')
    else:
        return render(request, template_name, context=context)


def checkout_success(request):
    template_name = 'orders/checkout_success.html'
    context = {}
    session_key = request.session.session_key
    order = Order.objects.filter(session_key=session_key)
    if order and session_key:
        order = order.latest(field_name="created")
        context['order'] = order
        return render(request, template_name, context=context)
    else:
        raise Http404


def single_order(request, *args, **kwargs):
    template_name = 'orders/single_order.html'
    context = {}
    print(request)
    print(request.GET)
    # hash_code = kwargs.get('hash_code')
    hash_code = request.GET.get('hash_code')
    statuses = Status.objects.all().order_by('number')
    context['statuses'] = statuses
    if hash_code:
        print('Accessing order by hash: {}'.format(hash_code))
        order = get_object_or_404(Order, hash_code=hash_code)
        context['order'] = order
    by_code = kwargs.get('code')
    return render(request, template_name, context=context)


class GenerateOrderPdf(View):
    def get(self, request, code, *args, **kwargs):
        context = {}
        # session_key = request.session.session_key
        order = get_object_or_404(Order, code=code)
        context['order'] = order
        pdf = render_to_pdf('orders/pdf/order.html', context)
        return HttpResponse(pdf, content_type='application/pdf')
