from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import get_object_or_404

from product.models import Department
from properties.models import Brand

# Create your views here.


def home(request):
    return render(request, 'landing/home.html')


def shop(request):
    department_list = Department.objects.all()
    return render(request, 'landing/shop.html', locals())


def department(request, department_slug):
    dep = get_object_or_404(Department, slug=department_slug)
    section_list = dep.get_sections()
    brands_list = dep.get_brands()
    return render(request, 'landing/department.html', locals())


def section(request, department_slug, section_slug):
    return render(request, 'landing/section.html')


def item_type(request, department_slug, section_slug, item_type_slug):
    return render(request, 'landing/item_type.html')


def item(request, department_slug, section_slug, item_type_slug, item_slug):
    return render(request, 'landing/item.html')
