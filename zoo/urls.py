from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('animals', views.animal, name='animals'),
    path('birds', views.birds, name='birds'),
    path(r'animals/(?P<id>\d+)/$', views.animal_detail, name='animal_detail'),
    path(r'birds/(?P<id>\d+)/$', views.bird_detail, name='bird_detail'),
    path('cart', views.cart, name='cart')
]
