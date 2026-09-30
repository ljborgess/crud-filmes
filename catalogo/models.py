from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Genero(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = 'gênero'
        verbose_name_plural = 'gêneros'
        ordering = ['nome']

    def __str__(self):
        return self.nome


class Diretor(models.Model):
    nome = models.CharField(max_length=100)
    nacionalidade = models.CharField(max_length=60)

    class Meta:
        verbose_name = 'diretor'
        verbose_name_plural = 'diretores'
        ordering = ['nome']

    def __str__(self):
        return self.nome


class Filme(models.Model):
    titulo = models.CharField(max_length=100)
    # PROTECT: um gênero ou diretor não pode ser apagado enquanto tiver filmes.
    genero = models.ForeignKey(Genero, on_delete=models.PROTECT, related_name='filmes')
    diretor = models.ForeignKey(Diretor, on_delete=models.PROTECT, related_name='filmes')
    sinopse = models.TextField(max_length=280)

    class Meta:
        ordering = ['titulo']

    def __str__(self):
        return self.titulo

    @property
    def media_nota(self):
        """Média das notas do filme, ou None se ainda não foi avaliado."""
        notas = [avaliacao.nota for avaliacao in self.avaliacoes.all()]
        if not notas:
            return None
        return sum(notas) / len(notas)


class Avaliacao(models.Model):
    # CASCADE: uma avaliação só existe em função do filme — sem ele, não significa nada.
    filme = models.ForeignKey(Filme, on_delete=models.CASCADE, related_name='avaliacoes')
    autor = models.CharField(max_length=80)
    nota = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        help_text='De 1 a 5 estrelas.',
    )
    comentario = models.TextField(max_length=280, blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'avaliação'
        verbose_name_plural = 'avaliações'
        ordering = ['-criado_em']

    def __str__(self):
        return f'{self.autor} — {self.nota}/5 em {self.filme.titulo}'

    @property
    def estrelas_cheias(self):
        return range(self.nota)

    @property
    def estrelas_vazias(self):
        return range(5 - self.nota)
