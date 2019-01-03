from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views import View
from product.models import Department
from product.models import Section
from product.models import Item
from product.models import ItemType
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


class ViewByItemType(View):
    template_name = 'landing/catalogue_and_sidebar/item_type.html'

    def get_context_data(self, request, department_slug, section_slug, item_type_slug, *args, **kwargs):
        department_obj = get_object_or_404(Department, slug=department_slug)
        section_obj = get_object_or_404(Section, slug=section_slug)
        item_type_obj = get_object_or_404(ItemType, slug=item_type_slug)
        sidebar = item_type_obj.get_sidebar()

        items_list = item_type_obj.get_items()
        product_filter = ProductFilter(request.GET, queryset=items_list)
        form = product_filter.form
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

        context = locals()

        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(request, *args, **kwargs)
        return render(request, self.template_name, context=context)


class ViewSingleItem(ViewByItemType):
    template_name = 'landing/catalogue_and_sidebar/item_single.html'

    def get_context_data(self, *args, **kwargs):

        context = super(ViewSingleItem, self).get_context_data(*args, **kwargs)
        item = get_object_or_404(Item, slug=self.kwargs['item_slug'])
        context['item'] = item
        sizes = get_object_or_404(Item, slug=self.kwargs['item_slug']).available_sizes.all()
        context['sizes'] = sizes
        return context