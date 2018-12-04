from django.db import models

# Create your models here.

class Animal(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.name

class Bird(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.name

# class Product(models.Model):
#     name = models.CharField(max_length=50)
#     description = models.CharField(max_length=150)
#     image = models.ImageField(blank=True, null=True)
#
# class Cart(models.Model):
#     user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
