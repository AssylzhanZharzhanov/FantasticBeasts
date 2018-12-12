from django.db import models
from zoo.models import Beast

# Create your models here.

class Profile(models.Model):
    account = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    items = models.ForeignKey(Beast, on_delete=models.CASCADE)
    #