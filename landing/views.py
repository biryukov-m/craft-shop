from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import get_object_or_404

from product.models import Department

# Create your views here.


def home(request):
    return render(request, 'landing/home.html')


def shop(request):
    department_list = Department.objects.all()
    return render(request, 'landing/shop.html', locals())


def department(request, slug):
    dep = get_object_or_404(Department, slug=slug)
    section_list = dep.get_sections()
    return render(request, 'landing/department.html', locals())



def section(request):
    return render(request, 'landing/section.html')


def item_type(request):
    return render(request, 'landing/item_type.html')


def item(request):
    return render(request, 'landing/item.html')
