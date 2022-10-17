from django.shortcuts import render

from clients.models import Client




# Create your views here.

def clients(request):
    context = {'clients': Client.objects.all()}
    return render(request, 'clients.html', context)


def client_details(request, client_id):
    client = Client.objects.get(id=client_id)
    context = {
        'client': client,
        'addresses': client.addresses.all()
    }
    return render(request, 'client_detail.html', context)

def cart(request, client_id):
    client = Client.objects.get(id=client_id)
    context = {
        'client': client,
        'cart': client.cart.all(),
        'product': product
    }
    return render(request, 'test.html', context)

