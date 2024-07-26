from django.shortcuts import render
from django.http import HttpResponse
from .models import Animais

def animais_2_anos(request):
    animais = Animal.objects.filter(idade=2)
    return HttpResponse(animais)

def animais_raca_gato_peso_maior_1kg(request):
    animais = Animal.objects.filter(raca='gato', peso__gt=1000)
    return HttpResponse(animais)

def animais_idade_entre_3_e_9(request):
    animais = Animal.objects.filter(idade__range=(3, 9))
    return HttpResponse(animais) 

def animais_machos(request):
    animais = Animal.objects.filter(sexo='M')
    return HttpResponse(animais)

def ultimo_animal_cadastrado(request):
    ultimo_animal = Animal.objects.last()
    return HttpResponse(ultimo_animal)



