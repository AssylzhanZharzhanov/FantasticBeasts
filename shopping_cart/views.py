from django.shortcuts import render
from .models import Cart
from .models import Beast
from django.contrib.auth.models import User


def add_to_cart(request,id):
    item = Beast.objects.get(id = id)
    cart = Cart.objects.get(owner__username=request.user)
    cart.items.add(item)


def cart(request):
    user_cart = Cart.objects.get(owner__username=request.user)
    items = user_cart.items.all()
    # amount_items = items.count() 'amount': amount_items
    return render(request, 'zoo/cart.html', {'items': items,})
