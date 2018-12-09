from django.contrib import admin
from .models import Beast


class BeastAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'description', 'image', 'views')
    list_filter = ('type', 'name',)
    search_fields = ('name', 'type',)
    ordering = ['views']


admin.site.register(Beast, BeastAdmin)

