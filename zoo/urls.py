from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('animals/', views.animal, name='animals'),
    path('birds/', views.birds, name='birds'),
    path(r'animals/<int:id>', views.animal_detail, name='animal_detail'),
    path(r'birds/<int:id>', views.bird_detail, name='bird_detail'),
    # path('cart', views.cart, name='cart'),
    path('search', views.search, name='search'),
    path('insects/', views.insect, name='insects'),
    path('insects/<int:id>', views.insect_detail, name='insect_detail'),
]
