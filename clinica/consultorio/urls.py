from django.urls import path
from . import views

urlpatterns = [
    path('animais/2-anos/', views.animais_2_anos, name='animais_2_anos'),
    path('animais/raca-gato-peso-maior-1kg/', views.animais_raca_gato_peso_maior_1kg, name='animais_raca_gato_peso_maior_1kg'),
    path('animais/idade-entre-3-e-9/', views.animais_idade_entre_3_e_9, name='animais_idade_entre_3_e_9'),
    path('animais/machos/', views.animais_machos, name='animais_machos'),
    path('ultimo-animal/', views.ultimo_animal_cadastrado, name='ultimo_animal'),
]