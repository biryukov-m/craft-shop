from django.shortcuts import render
from django.http import JsonResponse
from .models import ProductInBasket
from product.models import Item
from properties.models import Size


def basket_add(request):
    return_dict = dict()
    session_key = request.session.session_key
    data = request.POST
    item_id = data.get('item_id')
    item_quantity = int(data.get('item_quantity'))
    item_size = data.get('item_size')
    print('Ajax item size - ', item_size)
    item_size = Size.objects.get(name=item_size)
    print('Found in BD item size - ', item_size)
    item = Item.objects.get(id=item_id)
    new_product, created = ProductInBasket.objects.get_or_create(session_key=session_key,
                                                                 product=item,
                                                                 size=item_size,
                                                                 defaults={"quantity": item_quantity})
    if not created:
        new_product.quantity += item_quantity
        new_product.save(force_update=True)

    items_total_number = ProductInBasket.objects.filter(session_key=session_key).count()
    return_dict["items_total_number"] = items_total_number
    return JsonResponse(return_dict)


def basket_change_quantity(request):
    return_dict = dict()
    session_key = request.session.session_key
    data = request.POST
    item_id = data.get('item_id')
    print(item_id, 'item_id')
    print(item_id, 'item_id')
    item_quantity = int(data.get('item_quantity'))
    print(item_quantity, 'item_quantity')
    item_size = data.get('item_size')
    print(item_size, 'item_size')
    item_size = Size.objects.get(name=item_size)
    print(item_size, 'in BD item_size')
    item = Item.objects.get(id=item_id)
    print(item, 'item')
    method = data.get('method')
    print(method, 'method')
    print('Trying to find product')
    product = ProductInBasket.objects.get(session_key=session_key, product=item, size=item_size, quantity=item_quantity)
    print(product, 'Product')
    if product:
        print("if product - OK")
        if method == 'increase':
            product.quantity += 1
            product.save()
        elif method == 'decrease':
            if product.quantity > 1:
                product.quantity -= 1
                product.save()
            else:
                return_dict["response"] = ''''Wrong item quantity, can't decrease, because quantity <= 1'''
        else:
            return_dict["response"] = ''''Wrong method. Must be "decrease" or "increase"'''

    items_total_number = ProductInBasket.objects.filter(session_key=session_key).count()
    return_dict["items_total_number"] = items_total_number
    return JsonResponse(return_dict)


def basket_remove(request):
    return_dict = dict()
    session_key = request.session.session_key
    data = request.POST
    item_id = data.get('item_id')
    item_size = data.get('item_size')
    print('Delete Ajax item size - ', item_size)
    item_size = Size.objects.get(name=item_size)
    print('Delete. Found in BD item size - ', item_size)
    item = ProductInBasket.objects.get(session_key=session_key, id=item_id, size=item_size)
    item.delete()
    items_total_number = ProductInBasket.objects.filter(session_key=session_key).count()
    return_dict["items_total_number"] = items_total_number
    return JsonResponse(return_dict)


def checkout(request):
    session_key = request.session.session_key
    template_name = 'orders/checkout.html'
    if request.method == 'POST':
        return render(request, template_name)
    else:
        return render(request, template_name)
