from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('cart/', views.cart, name='cart'),
    path('add/<int:id>', views.add_to_cart, name='add_to_cart')
]
