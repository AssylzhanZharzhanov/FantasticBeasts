from django.urls import path, include
from . import views

urlpatterns = [
    path(r'register/', views.UserForm.as_view(), name='register'),
]
