from django.db import models


class Categoria(models.Model):
    nome = models.CharField(max_length=255)
    
    def __str__(self):
        return self.nome


class Contato(models.Model):
    nome = models.CharField(max_length=255)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    cpf = models.CharField(max_length=11)
    bio = models.TextField(blank=True)
    idade = models.IntegerField()
    altura = models.DecimalField(decimal_places=2, max_digits=3)
    ativo = models.BooleanField()

    def __str__(self):
        return self.nome
    
