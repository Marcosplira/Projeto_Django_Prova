from django.db import models

class Animais(models.Model):
    nome = models.CharField(max_length=100)
    raca = models.CharField(max_length=100)
    idade = models.IntegerField()
    peso = models.IntegerField()
    sexo = models.CharField(max_length=1)

    def __str__(self):
        return self.nome + ' '+ self.raca + ' ' + str(self.peso)


