from orders.models import Basket


def get_basket(request):
    session_key = request.session.session_key
    if not session_key:
        print("Didn't find session key, so we cycling new")
        request.session.cycle_key()
        return
    print('Trying to find basket with this session key {}'.format(session_key))
    if Basket.objects.filter(session_key=session_key, is_closed=False).exists():
        basket = Basket.objects.get(session_key=session_key, is_closed=False)
        print('Found basket, which is {}'.format(basket))
    else:
        print('Basket does not exist.')
        return {'get_basket': ''}
    print('Finding items in basket...')
    if basket.productinbasket_set.all().exists():
        items = basket.productinbasket_set.all()
        print('Item set is {}'.format(items))
        items_count = items.count()
        print('Item count is {}'.format(items_count))
        print('Trying to count total price...')
        basket_total_price = 0
        for i in items:
            basket_total_price += i.total_price
            print('{} total price is {}'.format(i, i.total_price))
        context = {'get_basket': {'items': items, 'items_count': items_count, 'basket_total_price': basket_total_price}}
        print('Returning context: {}'.format(context))
    else:
        print('Basket is empty.')
        return {'get_basket': ''}
    return context


