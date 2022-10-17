from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from products.models import Product, ProductCategory


def products(request):
    filters = request.GET.get('manufacturer', None)
    if filters is not None:
        context = {'products': Product.objects.filter(manufacturer__name__contains=(filters)), 'filters': filters}
    else:
        context = {'products': Product.objects.all(), 'filters': filters}

    return render(request, 'products.html', context)


def product_details(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {'product': product}
    return render(request, 'product_detail.html', context)

def categories(request):
    categories_objects = ProductCategory.objects.all()
    context = {'categories': categories_objects}
    return render(request, 'categories.html', context)

def product_category_details(request, category_id):
    category = ProductCategory.objects.get(id=category_id)
    return render(request, 'category_details.html', {'category': category})

