from django.contrib import admin
from .models import Cart
# Register your models here.


class CartAdmin(admin.ModelAdmin):
    list_display = ('owner', 'date_created')


admin.site.register(Cart, CartAdmin)