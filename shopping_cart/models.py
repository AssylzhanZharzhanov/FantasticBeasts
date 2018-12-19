from django.db import models
from django.contrib.auth.models import User
from zoo.models import Beast


class Cart(models.Model):
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    items = models.ManyToManyField(Beast)
    date_created = models.DateTimeField(auto_now=True)
    amount = models.IntegerField(default=1)
    #
    # def __str__(self):
    #     return self.o


def create_cart(request):
    user = User.objects.get(username=request.user)
    print(user)
    cart = Cart.objects.create(owner=user)
    cart.save()

