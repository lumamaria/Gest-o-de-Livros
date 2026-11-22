from django.shortcuts import render
from .models import Livro
from django.shortcuts import render, redirect
from .models import Livro, Autor, Genero
from .forms import LivroForm, AutorForm, GeneroForm

from django.shortcuts import render, get_object_or_404
from .models import Livro

def listar_livros(request):

    livros = Livro.objects.select_related(
        'autor',
        'genero'
    ).all()

    return render(
        request,
        'catalogo/listar_livros.html',
        {'livros': livros}
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
