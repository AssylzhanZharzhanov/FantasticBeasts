from django.shortcuts import render, get_object_or_404
from .models import Beast
from django.db.models import Q
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage


def search(request):
    if request.GET.get('search'):
        search_value = request.GET['search']
        animals = Beast.objects.filter(Q(name__icontains=search_value) | Q(name__startswith=search_value[0].upper()))
        context = {'animals': animals, 'search_value': search_value}
        return render(request, 'zoo/search.html', context)

    # return render(request, 'zoo/search.html')


def index(request):
    return render(request, 'zoo/index.html')


def animal(request):
    animals_list = Beast.objects.filter(type='Animal')
    paginator = Paginator(animals_list, 4)

    page = request.GET.get('page')
    animals = paginator.get_page(page)

    return render(request, 'zoo/animal.html', {'animals': animals})


def animal_detail(request, id):
    animal = Beast.objects.get(id=id)
    animal.views += 1
    animal.save()
    return render(request, 'zoo/animal_detail.html', {'animal': animal})


def birds(request):
    birds_list= Beast.objects.filter(type='Bird')
    paginator = Paginator(birds_list, 4)

    page = request.GET.get('page')
    birds = paginator.get_page(page)

    return render(request, 'zoo/bird.html', {'birds': birds})


def bird_detail(request, id):
    bird = Beast.objects.get(id=id)
    bird.views += 1
    bird.save()
    return render(request, 'zoo/bird_detail.html', {'bird': bird})


def insect(request):
    insects_list = Beast.objects.filter(type='Insect')
    paginator = Paginator(insects_list, 4)

    page = request.GET.get('page')
    insects = paginator.get_page(page)
    return render(request, 'zoo/insect.html', {'insects': insects})


def insect_detail(request, id):
    insect = Beast.objects.get(id=id)
    insect.views += 1
    insect.save()
    return render(request, 'zoo/insect_detail.html', {'insect': insect})

