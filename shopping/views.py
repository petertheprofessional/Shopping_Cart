from django.db.models import Sum
from django.shortcuts import render

# Create your views here.
from shopping.models import ShoppingCart


def cart(request, cart_id):
    cart = ShoppingCart.objects.get(id=cart_id)
    client_cart = cart.client
    products_cart = cart.products.all()
    total = cart.products.aggregate(Sum('price'))

    context = {
        'cart': cart,
        'client': client_cart,
        'products': products_cart,
        'total': total
    }
    return render(request, 'client_cart.html', context)
