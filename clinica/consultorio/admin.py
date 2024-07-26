from django.contrib import admin
from .models import Animais


class AnimalAdmin(admin.ModelAdmin):
    list_display = ('nome', 'raca', 'peso', 'idade', 'sexo')

admin.site.register(Animais, AnimalAdmin)

