from django.shortcuts import render,redirect, reverse, get_object_or_404
from .models import Cart
from .models import Beast
from django.contrib.auth.models import User


def add_to_cart(request,id):
    item = Beast.objects.get(id=id)
    user_cart = Cart.objects.get(owner__username=request.user)
    user_cart.items.add(item)
    user_cart.save()

    if item.type == 'Animal':
        return redirect('/animals')
    elif item.type == 'Bird':
        return redirect('/birds')
    else:
        return redirect('/insects')


def delete_from_cart(request, id):
    user_cart = Cart.objects.get(owner__username=request.user)
    item = Beast.objects.get(id=id)
    user_cart.items.remove(item)
    user_cart.save()
    return reverse('cart')


def cart(request):
    user_cart = get_object_or_404(Cart, owner__username=request.user)
    items = user_cart.items.all()
    amount_items = items.count()
    # 'amount': amount_items
    return render(request, 'zoo/cart.html', {'items': items,})


def refresh(request, id):
    amount = request.POST.get('number')


