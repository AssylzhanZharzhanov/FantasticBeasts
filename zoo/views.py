from django.shortcuts import render
from .models import Beast


def index(request):
    return render(request, 'zoo/index.html')


def animal(request):
    animals = Beast.objects.filter(type='Animal')
    return render(request, 'zoo/animal.html', {'animals': animals})


def animal_detail(request, id):
    animal = Beast.objects.get(id=id)
    return  render(request, 'zoo/animal_detail.html', {'animal': animal})


def birds(request):
    birds = Beast.objects.filter(type='Bird')
    return render(request, 'zoo/bird.html', {'birds': birds})


def bird_detail(request, id):
    bird = Beast.objects.get(id=id)
    return render(request, 'zoo/bird_detail.html', {'birds': bird})


def cart(request):
    return render(request, 'zoo/cart.html')

