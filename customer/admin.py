from django.contrib import admin
from .models import Drink

class DrinkAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')

admin.site.register(Drink, DrinkAdmin)
