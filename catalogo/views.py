
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .models import Livro, Autor, Genero
from .forms import LivroForm, AutorForm, GeneroForm


def listar_livros(request):
    livros = Livro.objects.select_related(
        'autor',
        'genero'
    ).all()

    # Pesquisa pelo título
    busca = request.GET.get('q', '')

    if busca:
        livros = livros.filter(titulo__icontains=busca)

    # Filtro por autor
    autor_selecionado = request.GET.get('autor', '')

    if autor_selecionado:
        livros = livros.filter(autor_id=autor_selecionado)

    # Filtro por gênero
    genero_selecionado = request.GET.get('genero', '')

    if genero_selecionado:
        livros = livros.filter(genero_id=genero_selecionado)

    # Ordenação dos livros
    livros = livros.order_by('titulo')

    # Paginação: 5 livros por página
    paginador = Paginator(livros, 5)
    numero_pagina = request.GET.get('page')
    pagina = paginador.get_page(numero_pagina)

    # Preservar os parâmetros da pesquisa e dos filtros
    parametros = request.GET.copy()
    parametros.pop('page', None)
    query_string = parametros.urlencode()

    # Autores e gêneros disponíveis nos filtros
    autores = Autor.objects.all().order_by('nome')
    generos = Genero.objects.all().order_by('nome')

    return render(
        request,
        'catalogo/listar_livros.html',
        {
            'livros': pagina,
            'autores': autores,
            'generos': generos,
            'busca': busca,
            'autor_selecionado': autor_selecionado,
            'genero_selecionado': genero_selecionado,
            'query_string': query_string,
        }
    )


def autores(request):
    form = AutorForm()

    if request.method == 'POST':
        form = AutorForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('autores')

    autores = Autor.objects.all()

    return render(request, 'catalogo/autores.html', {
        'form': form,
        'autores': autores
    })


def generos(request):
    form = GeneroForm()

    if request.method == 'POST':
        form = GeneroForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('generos')

    generos = Genero.objects.all()

    return render(request, 'catalogo/generos.html', {
        'form': form,
        'generos': generos
    })


def livros(request):
    form = LivroForm()

    if request.method == 'POST':
        form = LivroForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('livros')

    livros = Livro.objects.select_related(
        'autor', 'genero'
    ).all()

    return render(request, 'catalogo/livros.html', {
        'form': form,
        'livros': livros
    })


def detalhes_livro(request, id):
    livro = get_object_or_404(Livro, id=id)

    return render(request, 'catalogo/detalhes_livro.html', {
        'livro': livro
    })
