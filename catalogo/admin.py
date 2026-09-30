from django.contrib import admin

from .models import Avaliacao, Diretor, Filme, Genero


@admin.register(Genero)
class GeneroAdmin(admin.ModelAdmin):
    list_display = ('nome',)


@admin.register(Diretor)
class DiretorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'nacionalidade')


@admin.register(Filme)
class FilmeAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'genero', 'diretor')
    list_filter = ('genero', 'diretor')


@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ('filme', 'autor', 'nota', 'criado_em')
    list_filter = ('nota',)
