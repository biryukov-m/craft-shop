from urllib.parse import urlencode
url = 'http://127.0.0.1:8000/shop/clothes/men_clothes/men_shirt?tkanina=silk'
par = {'fabric': 'vasa'}

u = urlencode()
print(u)