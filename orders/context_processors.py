from orders.models import ProductInBasket


def get_basket(request):
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()
    items = ProductInBasket.objects.filter(session_key=session_key)
    items_count = items.count
    basket_total_price = 0
    for i in items:
        basket_total_price += i.total_price
    context = {'get_basket': {'items': items, 'items_count': items_count, 'basket_total_price': basket_total_price}}
    return context


