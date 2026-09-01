from django.db import models


class Genero(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nome


class Filme(models.Model):
    titulo = models.CharField(max_length=100)
    genero = models.ForeignKey(Genero, on_delete=models.PROTECT, related_name='filmes')
    sinopse = models.TextField(max_length=280)

    def __str__(self):
        return self.titulo
