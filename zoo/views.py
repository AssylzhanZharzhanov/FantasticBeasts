from django.shortcuts import render
from .models import Animal
from .models import Bird
# Create your views here.

def index(request):
    return render(request, 'zoo/index.html')

def animal(request):
    animals = Animal.objects.all()
    return render(request, 'zoo/animal.html', {'animals': animals})

def animal_detail(request, id):
    animal = Animal.objects.get(id=id)
    return  render(request, 'zoo/animal_detail.html', {'animal': animal})

def birds(request):
    birds = Bird.objects.all()
    return  render(request,'zoo/bird.html', {'birds':birds})

def bird_detail(request, id):
    bird = Bird.objects.get(id = id)
    return render(request, 'zoo/animal.html', {'birds': bird})

def cart(request):
    return render(request, 'zoo/cart.html')

