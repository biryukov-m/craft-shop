from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import get_object_or_404

from product.models import Department
from product.models import Item
from product.models import ItemType

from properties.models import Gender
from properties.models import Brand
from properties.models import Fabric
from properties.models import Color
from properties.models import Size

# Create your views here.


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


def item_type(request, department_slug, section_slug, item_type_slug):

    department_obj = get_object_or_404(Department, slug=department_slug)
    sections = department_obj.get_sections()
    sections_and_item_types = {}
    for sec in sections:
        for it in sec.get_item_types():
            if it in sections_and_item_types:
                sections_and_item_types[sec].append(it)
            else:
                sections_and_item_types[sec] = [it]
    fabrics = Fabric.objects.all()
    genders = Gender.objects.all()
    colors = Color.objects.all()
    brands = Brand.objects.all()
    sizes = Size.objects.all()

    item_type_obj = get_object_or_404(ItemType, slug=item_type_slug)
    items_list = item_type_obj.get_items()
    return render(request, 'landing/item_type.html', locals())


def item(request, department_slug, section_slug, item_type_slug, item_slug):
    return render(request, 'landing/item.html')
