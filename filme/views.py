from django.shortcuts import render, redirect, get_object_or_404
from .models import Filme, Genero


def lista_filmes(request):
    filmes = Filme.objects.select_related('genero').all()
    return render(request, 'filme/lista.html', {'filmes': filmes})


def criar_filme(request):
    if request.method == 'POST':
        titulo = request.POST['titulo']
        genero_id = request.POST['genero']
        sinopse = request.POST.get('sinopse', '')

        Filme.objects.create(titulo=titulo, genero_id=genero_id, sinopse=sinopse)
        return redirect('lista_filmes')

    generos = Genero.objects.all()
    return render(request, 'filme/form_filme.html', {'titulo_pagina': 'Novo Filme', 'generos': generos})


def editar_filme(request, pk):
    filme = get_object_or_404(Filme, pk=pk)

    if request.method == 'POST':
        filme.titulo = request.POST['titulo']
        filme.genero_id = request.POST['genero']
        filme.sinopse = request.POST.get('sinopse', '')
        filme.save()
        return redirect('lista_filmes')

    generos = Genero.objects.all()
    return render(request, 'filme/form_filme.html', {'filme': filme, 'titulo_pagina': f'Editar: {filme.titulo}', 'generos': generos})


def excluir_filme(request, pk):
    filme = get_object_or_404(Filme, pk=pk)

    if request.method == 'POST':
        filme.delete()
        return redirect('lista_filmes')

    return render(request, 'filme/confirmar_exclusao.html', {'filme': filme})
