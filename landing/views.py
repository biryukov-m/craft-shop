from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import get_object_or_404

from product.models import Department
from product.models import Section
from product.models import Item
from product.models import ItemType

from properties.models import Gender
from properties.models import Brand
from properties.models import Fabric
from properties.models import Color
from properties.models import Size

from django.db.models import Max, Min

from product.forms import ProductFilter


def home(request):
    return render(request, 'landing/home.html')


def shop(request):
    sections_in_departments = {}
    for dep in Department.objects.all():
        for sec in dep.get_sections():
            if dep not in sections_in_departments:
                sections_in_departments[dep] = [sec]
            else:
                sections_in_departments[dep].append(sec)
    return render(request, 'landing/shop.html', locals())


def section(request, department_slug, section_slug):
    return render(request, 'landing/section.html')


def department(request, department_slug, section_slug):
    return render(request, 'landing/department.html')


def item_type(request, department_slug, section_slug, item_type_slug):
    department_obj = get_object_or_404(Department, slug=department_slug)
    section_obj = get_object_or_404(Section, slug=section_slug)
    sections = department_obj.get_sections()
    sections_and_item_types = {}
    for sec in sections:
        for it in sec.get_item_types():
            if sec in sections_and_item_types:
                sections_and_item_types[sec].append(it)
            else:
                sections_and_item_types[sec] = [it]

    item_type_obj = get_object_or_404(ItemType, slug=item_type_slug)
    items_list = item_type_obj.get_items()

    filter = ProductFilter(request.GET, queryset=items_list)

    form = filter.form
      
    # Аггрегация макс и мин цены из всего списка товаров
    min_price = items_list.aggregate(Min('price'))
    max_price = items_list.aggregate(Max('price'))

    # Достать из аггрегации конкретные значения цен
    try:
        min_price = int(min_price['price__min'])
        max_price = int(max_price['price__max'])
    except TypeError:
        min_price, max_price = 0, 0

    if 'price_min' in request.GET:
        current_min_price = request.GET.get('price_min')
    else:
        current_min_price = min_price

    if 'price_max' in request.GET:
        current_max_price = request.GET.get('price_max')
    else:
        current_max_price = max_price

    return render(request, 'landing/item_type.html', locals())


def item(request, department_slug, section_slug, item_type_slug, item_slug):
    return render(request, 'landing/item.html', {'filter': filter})


def product_list(request):
    filter = ProductFilter(request.GET, queryset=Item.objects.all())
    return render(request, 'landing/filter.html', {'filter': filter})