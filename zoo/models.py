from django.db import models


class Beast(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    image = models.ImageField(blank=True, null=True)
    views = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    Animal = 'Animal'
    Bird = 'Bird'
    Insect = 'Insect'
    YEAR_IN_SCHOOL_CHOICES = (
        (Animal, 'Animal'),
        (Bird, 'Bird'),
        (Insect, 'Insect'),
    )
    type = models.CharField(
        max_length=10,
        choices=YEAR_IN_SCHOOL_CHOICES,
    )

    def __str__(self):
        return self.name

# class Type(models.Model):
#    type =
# class Bird(models.Model):
#     name = models.CharField(max_length=50)
#     description = models.CharField(max_length=150)
#     image = models.ImageField(blank=True, null=True)
#     views = models.IntegerField(default=0)
#     type = models.CharField(max_length=50)
#
#     def __str__(self):
#         return self.name


# class Product(models.Model):
#     name = models.CharField(max_length=50)
#     description = models.CharField(max_length=150)
#     image = models.ImageField(blank=True, null=True)
#
# class Cart(models.Model):
#     user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
