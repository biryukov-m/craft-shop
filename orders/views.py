from django.shortcuts import render
from django.http import JsonResponse
from .models import ProductInBasket
from product.models import Item

# Create your views here.


def basket_add(request):
    return_dict = dict()
    session_key = request.session.session_key
    data = request.POST
    item_id = data.get('item_id')
    item_quantity = int(data.get('item_quantity'))
    print(item_quantity)
    item = Item.objects.get(id=item_id)
    print(item)
    new_product = ProductInBasket.objects.create(session_key=session_key,
                                                 product=item,
                                                 quantity=item_quantity)
    new_product.save()

    items_total_number = ProductInBasket.objects.filter(session_key=session_key, is_inactive=False).count()
    return_dict["items_total_number"] = items_total_number
    return JsonResponse(return_dict)


def basket_remove(request):
    return_dict = dict()
    session_key = request.session.session_key
    data = request.POST
    item_id = data.get('item_id')
    item = ProductInBasket.objects.get(session_key=session_key, id=item_id)
    item.is_inactive = True
    item.save()
    items_total_number = ProductInBasket.objects.filter(session_key=session_key, is_inactive=False).count()
    return_dict["items_total_number"] = items_total_number
    return JsonResponse(return_dict)
